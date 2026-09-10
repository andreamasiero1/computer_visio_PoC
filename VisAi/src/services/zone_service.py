import cv2
import numpy as np

class ZoneService:
    def __init__(self):
        # Linee di conteggio configurate dal Presentation Layer
        self._counting_lines: list[dict] = []
        
        print("✅ ZoneService: Inizializzato.")
    
    def applyMask(self, frame, zones: list):
        """
        Applica una maschera al frame, oscurando le aree definite in zones.
        I pixel all'interno delle zone vengono azzerati (nero).
        
        Args:
            frame: Il frame video (numpy array BGR).
            zones: Lista di zone. Ogni zona è un dict con chiave "points",
                   che contiene una lista di tuple (x, y) che definiscono un poligono.
                   Es: [{"points": [(0,0), (100,0), (100,100), (0,100)]}]
        
        Returns:
            Il frame con le zone oscurate.
        """
        if frame is None or not zones:
            return frame
        
        for zone in zones:
            points = zone.get("points")
            if not points:
                continue
            
            # Converti i punti in un array numpy (formato richiesto da fillPoly)
            pts = np.array(points, dtype=np.int32)
            
            # Oscura l'area del poligono (riempila di nero)
            cv2.fillPoly(frame, [pts], (0, 0, 0))
        
        return frame
    
    def set_counting_lines(self, lines: list[dict]) -> None:
        """
        Riceve le linee di conteggio dal Presentation Layer e le memorizza.
        Il MainService le leggerà e le passerà al CountService.
        
        Args:
            lines: Lista di linee. Ogni linea è un dict:
                   {"name": "ingresso", "orientation": "vertical", "position": 960, "in_direction": "right"}
        """
        self._counting_lines = lines
        print(f"ZoneService: Memorizzate {len(lines)} linee di conteggio.")
    
    def get_counting_lines(self) -> list[dict]:
        """Restituisce le linee di conteggio configurate."""
        return self._counting_lines

