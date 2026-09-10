import cv2
import mediapipe as mp
import os
import urllib.request
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class BlurService:
    def __init__(self, blur_strength: int = 99, detection_confidence: float = 0.3):
        """
        Servizio per la sfocatura dei volti (privacy GDPR).
        Usa MediaPipe Face Detection di Google per un rilevamento robusto
        anche con occlusioni parziali (mano sulla bocca, cappelli, occhiali).
        
        Args:
            blur_strength: Intensità della sfocatura gaussiana. Deve essere un numero dispari.
                           Valori consigliati: 51 (leggero), 99 (forte), 151 (molto forte).
            detection_confidence: Soglia di confidenza per il rilevamento del volto (0.0 - 1.0).
                                  Più bassa = rileva più volti ma con più falsi positivi.
                                  Consigliato: 0.3-0.5
        """
        # Assicura che il valore sia dispari (requisito di GaussianBlur)
        if blur_strength % 2 == 0:
            blur_strength += 1
        self.blur_strength = blur_strength
        
        model_path = "blaze_face_short_range.tflite"
        if not os.path.exists(model_path):
            print(f"Scaricamento del modello MediaPipe Face Detection in {model_path}...")
            urllib.request.urlretrieve("https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite", model_path)
            
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.FaceDetectorOptions(base_options=base_options, min_detection_confidence=detection_confidence)
        self._face_detector = vision.FaceDetector.create_from_options(options)
        
        print(f"✅ BlurService: MediaPipe Face Detection caricato (blur_strength={self.blur_strength}, confidence={detection_confidence}).")
    
    def applyBlur(self, frame, detections: list = None):
        """
        Rileva i volti nel frame e li sfoca per garantire la privacy.
        
        Opera SOLO all'interno dei bounding box delle persone rilevate da YOLO.
        Se non ci sono detections, restituisce il frame intatto (zero spreco CPU).
        
        Args:
            frame: Il frame video (numpy array BGR).
            detections: Lista di detections dal PersonService.
                        Ogni detection è un dict con chiave "position": {x1, y1, x2, y2}.
        
        Returns:
            Il frame con i volti sfocati.
        """
        if frame is None or not detections:
            return frame
        
        for det in detections:
            pos = det["position"]
            x1, y1, x2, y2 = pos["x1"], pos["y1"], pos["x2"], pos["y2"]
            
            # Ritaglia la regione della persona
            person_roi = frame[y1:y2, x1:x2]
            if person_roi.size == 0:
                continue
            
            roi_h, roi_w = person_roi.shape[:2]
            
            # MediaPipe richiede input in RGB
            rgb_roi = cv2.cvtColor(person_roi, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_roi)
            results = self._face_detector.detect(mp_image)
            
            if results.detections:
                for detection in results.detections:
                    # MediaPipe Tasks restituisce coordinate assolute per il bounding box
                    bbox = detection.bounding_box
                    
                    fx = int(bbox.origin_x)
                    fy = int(bbox.origin_y)
                    fw = int(bbox.width)
                    fh = int(bbox.height)
                    
                    # Aggiungi un padding del 20% per coprire meglio il volto
                    pad_w = int(fw * 0.2)
                    pad_h = int(fh * 0.2)
                    fx = max(0, fx - pad_w)
                    fy = max(0, fy - pad_h)
                    fw = min(roi_w - fx, fw + 2 * pad_w)
                    fh = min(roi_h - fy, fh + 2 * pad_h)
                    
                    # Riporta le coordinate al frame originale
                    abs_fx = x1 + fx
                    abs_fy = y1 + fy
                    
                    face_region = frame[abs_fy:abs_fy + fh, abs_fx:abs_fx + fw]
                    if face_region.size > 0:
                        frame[abs_fy:abs_fy + fh, abs_fx:abs_fx + fw] = cv2.GaussianBlur(
                            face_region,
                            (self.blur_strength, self.blur_strength),
                            30
                        )
        
        return frame
