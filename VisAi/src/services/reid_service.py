import numpy as np
import cv2
import time

class ReIDService:
    """
    Servizio di Re-Identification.
    Usa un modello di feature extraction per generare un "embedding" (vettore numerico)
    che descrive l'aspetto visivo di una persona. Confrontando gli embedding tra telecamere
    diverse, è possibile ri-identificare la stessa persona con un ID globale.
    """
    
    def __init__(self, similarity_threshold: float = 0.6, max_lost_seconds: float = 30.0):
        """
        Args:
            similarity_threshold: Soglia di similarità coseno (0-1). 
                                  Più alta = più restrittivo (meno falsi positivi, più falsi negativi).
                                  Consigliato: 0.5-0.7
            max_lost_seconds: Dopo quanti secondi una persona "scomparsa" viene dimenticata dal registro.
        """
        self.similarity_threshold = similarity_threshold
        self.max_lost_seconds = max_lost_seconds
        
        # Registro globale: { global_id: { "embedding": np.array, "last_seen": timestamp, "camera_id": str } }
        self._registry: dict[int, dict] = {}
        self._next_global_id = 1
        
        # Mappa da (camera_id, local_track_id) → global_id (cache per non ricalcolare ogni frame)
        self._local_to_global: dict[tuple, int] = {}
        
        # Carica il modello di feature extraction
        self._load_model()
    
    def _load_model(self):
        """
        Carica il modello per estrarre le feature (embedding) dalle immagini delle persone.
        Usiamo un MobileNetV2 pre-addestrato su ImageNet come feature extractor.
        È leggero (gira bene anche su CPU) e produce embedding ragionevolmente buoni.
        
        Per risultati migliori in produzione, sostituire con un modello Re-ID dedicato
        come OSNet (da torchreid) o CLIP.
        """
        import torch
        import torchvision.models as models
        import torchvision.transforms as transforms
        
        print("ReIDService: Caricamento modello feature extractor (MobileNetV2)...")
        
        # MobileNetV2 senza il layer di classificazione finale → produce un vettore di 1280 dimensioni
        mobilenet = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
        # Rimuoviamo il classificatore, teniamo solo il feature extractor
        self._model = torch.nn.Sequential(
            mobilenet.features,
            torch.nn.AdaptiveAvgPool2d((1, 1)),
            torch.nn.Flatten()
        )
        self._model.eval()  # Modalità inferenza (no training)
        
        # Trasformazione standard per le immagini in input al modello
        self._transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        
        # Determina il device (MPS per Apple Silicon, altrimenti CPU)
        if torch.backends.mps.is_available():
            self._device = torch.device("mps")
        else:
            self._device = torch.device("cpu")
        
        self._model = self._model.to(self._device)
        self._torch = torch  # Salva riferimento per usarlo nei metodi
        
        print(f"ReIDService: Modello caricato con successo su {self._device}.")
    
    def extract_features(self, person_crop: np.ndarray) -> np.ndarray:
        """
        Estrae un vettore di embedding (feature vector) da un ritaglio di persona.
        
        Args:
            person_crop: Immagine BGR (numpy array) ritagliata attorno alla persona.
            
        Returns:
            Un vettore numpy normalizzato di 1280 dimensioni.
        """
        if person_crop is None or person_crop.size == 0:
            return None
            
        # Converti da BGR (OpenCV) a RGB (PyTorch)
        rgb_crop = cv2.cvtColor(person_crop, cv2.COLOR_BGR2RGB)
        
        # Applica le trasformazioni e aggiungi la dimensione batch
        input_tensor = self._transform(rgb_crop).unsqueeze(0).to(self._device)
        
        # Estrai le feature senza calcolare i gradienti (più veloce, meno memoria)
        with self._torch.no_grad():
            features = self._model(input_tensor)
        
        # Converti in numpy e normalizza (L2 norm) per usare la similarità coseno
        embedding = features.cpu().numpy().flatten()
        norm = np.linalg.norm(embedding)
        if norm > 0:
            embedding = embedding / norm
            
        return embedding
    
    def match(self, embedding: np.ndarray, camera_id: str, local_track_id: int) -> int:
        """
        Confronta l'embedding di una persona con il registro globale.
        Se trova un match sopra la soglia, restituisce il global_id esistente.
        Altrimenti, assegna un nuovo global_id.
        
        Args:
            embedding: Il vettore feature della persona.
            camera_id: Identificativo della telecamera (es. "cam_01").
            local_track_id: L'ID di tracking locale assegnato da YOLO su questa telecamera.
            
        Returns:
            Il global_id (ID univoco cross-camera) della persona.
        """
        # Prima pulizia: rimuovi persone "scadute" dal registro
        self._cleanup_registry()
        
        # Controlla se abbiamo già mappato questo (camera, local_id) di recente
        cache_key = (camera_id, local_track_id)
        if cache_key in self._local_to_global:
            global_id = self._local_to_global[cache_key]
            # Aggiorna l'embedding e il timestamp nel registro
            if global_id in self._registry:
                # Usa una media mobile (EMA) per aggiornare l'embedding, fondendo le nuove feature con quelle storiche
                alpha = 0.9
                updated_emb = alpha * self._registry[global_id]["embedding"] + (1.0 - alpha) * embedding
                self._registry[global_id]["embedding"] = updated_emb / np.linalg.norm(updated_emb)
                
                self._registry[global_id]["last_seen"] = time.time()
                self._registry[global_id]["camera_id"] = camera_id
                return global_id
        
        # Cerca il match migliore nel registro globale
        best_match_id = None
        best_similarity = -1.0
        
        for global_id, entry in self._registry.items():
            similarity = self._cosine_similarity(embedding, entry["embedding"])
            if similarity > best_similarity:
                best_similarity = similarity
                best_match_id = global_id
        
        # Se il match supera la soglia → è la stessa persona
        if best_match_id is not None and best_similarity >= self.similarity_threshold:
            # Usa una media mobile (EMA) per fondere le nuove feature con quelle storiche
            alpha = 0.9
            updated_emb = alpha * self._registry[best_match_id]["embedding"] + (1.0 - alpha) * embedding
            self._registry[best_match_id]["embedding"] = updated_emb / np.linalg.norm(updated_emb)
            
            self._registry[best_match_id]["last_seen"] = time.time()
            self._registry[best_match_id]["camera_id"] = camera_id
            self._local_to_global[cache_key] = best_match_id
            return best_match_id
        
        # Altrimenti → nuova persona, assegna un nuovo ID globale
        new_global_id = self._next_global_id
        self._next_global_id += 1
        
        self._registry[new_global_id] = {
            "embedding": embedding,
            "last_seen": time.time(),
            "camera_id": camera_id
        }
        self._local_to_global[cache_key] = new_global_id
        
        return new_global_id
    
    def get_active_persons(self) -> dict:
        """Restituisce il registro delle persone attualmente tracciate."""
        self._cleanup_registry()
        return {
            gid: {"camera_id": entry["camera_id"], "last_seen": entry["last_seen"]}
            for gid, entry in self._registry.items()
        }
    
    def _cosine_similarity(self, vec_a: np.ndarray, vec_b: np.ndarray) -> float:
        """Calcola la similarità coseno tra due vettori normalizzati."""
        return float(np.dot(vec_a, vec_b))
    
    def _cleanup_registry(self):
        """Rimuove dal registro le persone non viste da più di max_lost_seconds."""
        now = time.time()
        expired_ids = [
            gid for gid, entry in self._registry.items()
            if (now - entry["last_seen"]) > self.max_lost_seconds
        ]
        for gid in expired_ids:
            del self._registry[gid]
        
        # Pulisci anche la cache locale
        expired_local = [
            key for key, gid in self._local_to_global.items()
            if gid not in self._registry
        ]
        for key in expired_local:
            del self._local_to_global[key]
