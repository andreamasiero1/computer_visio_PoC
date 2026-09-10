import cv2
import sys
import os

# Assicura che Python trovi il modulo 'src'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.services.person_service import PersonService
from src.core.interfaces import Listener

# 1. Creiamo un "finto" Listener solo per vedere se gli eventi arrivano correttamente
class DummyListener(Listener):
    def update(self, event_data: dict) -> None:
        print(f"🎯 [EVENTO LISTENER] Ricevuto: {event_data}")

def main():
    print("Inizializzazione del PersonService...")
    person_service = PersonService()
    
    # Colleghiamo il nostro listener di test
    dummy_listener = DummyListener()
    person_service.addListener(dummy_listener)
    
    # 2. Apriamo la webcam (0 è la telecamera integrata del Mac)
    # Se preferisci testare su un video registrato, cambia 0 con "nome_video.mp4"
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Errore: Impossibile aprire la webcam.")
        return

    print("✅ Webcam aperta! Premi 'q' sulla finestra del video per chiudere.")

    while True:
        # Leggiamo il frame dalla webcam
        ret, frame = cap.read()
        if not ret:
            print("Errore nella lettura del frame.")
            break
            
        # 3. Passiamo il frame al servizio!
        # Il detectAndTrack disegnerà i box sul frame e notificherà il DummyListener
        processed_frame = person_service.detectAndTrack(frame)
        
        # 4. Mostriamo il risultato
        cv2.imshow("Test Person Service - YOLOv8", processed_frame)
        
        # Premi 'q' per uscire
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Chiusura pulita
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
