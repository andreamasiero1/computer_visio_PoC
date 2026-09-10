import cv2
from ultralytics import YOLO
from src.core.interfaces import Listener

class PersonService:
    # Se hai un tuo modello allenato su colab, passa il path a 'best.pt'
    # Altrimenti lascia 'yolov8n.pt' e lo scaricherà da solo al primo avvio.
    def __init__(self, model_path: str = 'yolov8n.pt'):
        self.listeners: list[Listener] = []
        
        print(f"Caricamento del modello YOLO da {model_path} in corso...")
        self.model = YOLO(model_path)
        print("Modello caricato con successo.")

    def addListener(self, listener: Listener) -> None:
        """Aggiunge un listener (es. CountService) da notificare."""
        self.listeners.append(listener)

    def detectAndTrack(self, frame):
        """
        Elabora il frame, rileva le persone e le traccia assegnando un ID.
        
        Returns:
            tuple: (frame_processato, lista_detections)
                   Ogni detection è un dict con: local_track_id, position, crop (ritaglio immagine)
        """
        detections = []
        
        # 1. Inferenza con Tracker Integrato
        # persist=True fa ricordare a YOLO le persone tra un frame e l'altro
        # classes=[0] dice a YOLO di cercare SOLO persone (ignorando cani, auto, ecc.)
        results = self.model.track(frame, persist=True, classes=[0], verbose=False)

        # 2. Estrazione dati dal risultato
        if len(results) > 0:
            result = results[0]
            
            # Se ci sono bounding box E hanno un ID di tracciamento assegnato
            if result.boxes is not None and result.boxes.id is not None:
                # Estraiamo le coordinate e gli ID convertendoli in numeri semplici
                boxes = result.boxes.xyxy.cpu().numpy()
                track_ids = result.boxes.id.int().cpu().numpy()
                
                for box, track_id in zip(boxes, track_ids):
                    x1, y1, x2, y2 = map(int, box)
                    
                    # Ritaglia l'immagine della persona dal frame (crop)
                    person_crop = frame[y1:y2, x1:x2].copy()
                    
                    # -- OPZIONALE: Disegna a schermo per debug visivo --
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"ID: {track_id}", (x1, y1 - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                    detection = {
                        "local_track_id": int(track_id),
                        "position": {"x1": x1, "y1": y1, "x2": x2, "y2": y2},
                        "crop": person_crop
                    }
                    detections.append(detection)
                    
                    # 3. Notifica i Listener
                    event_data = {
                        "event_type": "person_tracked",
                        "person_id": int(track_id),
                        "position": {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
                    }
                    self.notifyListeners(event_data)
            
        return frame, detections

    def notifyListeners(self, event_data: dict):
        for listener in self.listeners:
            listener.update(event_data)
