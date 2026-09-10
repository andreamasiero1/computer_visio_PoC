from src.core.interfaces import ICounterRepository
from src.services.blur_service import BlurService
from src.services.zone_service import ZoneService
from src.services.person_service import PersonService
from src.services.reid_service import ReIDService
import cv2

class MainService:
    def __init__(
        self,
        repository: ICounterRepository,
        blur_service: BlurService,
        zone_service: ZoneService,
        person_service: PersonService,
        reid_service: ReIDService = None,
        camera_id: str = "cam_default"
    ):
        """
        Orchestratore principale. Riceve le dipendenze in ingresso (Dependency Injection).
        """
        self.repository = repository
        self.blur_service = blur_service
        self.zone_service = zone_service
        self.person_service = person_service
        self.reid_service = reid_service
        self.camera_id = camera_id
        self.black_zones = []
        self.dark_zones = []

    def getStats(self) -> list:
        """
        Recupera le statistiche (conteggi) tramite il repository fornito.
        """
        return self.repository.get_counts()

    def setBlackZones(self, zones: list) -> None:
        """
        Imposta le zone nere che verranno utilizzate per mascherare i frame.
        """
        self.black_zones = zones

    def setDarkZones(self, zones: list) -> None:
        """
        Imposta le zone scure che verranno utilizzate per mascherare i frame.
        """
        self.dark_zones = zones
        
    def process_frame(self, frame):
        """
        Orchestra l'elaborazione di un singolo frame video:
        1. Applica le maschere (black/dark zones)
        2. Esegue la detection e il tracking 
        3. Se disponibile, esegue il Re-ID per ottenere un ID globale cross-camera
        4. Applica filtri privacy (blur)
        """
        # 1. Maschera le zone da ignorare
        masked_frame = self.zone_service.applyMask(frame, self.black_zones)
        masked_frame = self.zone_service.applyMask(masked_frame, self.dark_zones)
        
        # 2. Rilevamento e tracking (ora restituisce anche le detections con i crop)
        tracked_frame, detections = self.person_service.detectAndTrack(masked_frame)
        
        # 3. Re-Identification cross-camera (se il servizio è stato fornito)
        if self.reid_service is not None and len(detections) > 0:
            for det in detections:
                crop = det["crop"]
                local_id = det["local_track_id"]
                pos = det["position"]
                
                # Estrai le feature e cerca un match globale
                embedding = self.reid_service.extract_features(crop)
                if embedding is not None:
                    global_id = self.reid_service.match(embedding, self.camera_id, local_id)
                    
                    # Sovrascrivi l'etichetta sul frame con il Global ID
                    cv2.putText(
                        tracked_frame, 
                        f"GID: {global_id}", 
                        (pos["x1"], pos["y2"]),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 200, 255), 2
                    )
        
        # 4. Privacy (sfocatura volti nelle aree delle persone rilevate)
        final_frame = self.blur_service.applyBlur(tracked_frame, detections)
        
        return final_frame

