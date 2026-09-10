import cv2
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.repositories.in_memory_counter_repository import InMemoryCounterRepository
from src.services.blur_service import BlurService
from src.services.zone_service import ZoneService
from src.services.person_service import PersonService
from src.services.count_service import CountService
from src.services.reid_service import ReIDService
from src.services.main_service import MainService

def main():
    print("=" * 50)
    print("TEST Re-ID Service con MainService")
    print("=" * 50)
    
    # 1. Setup Repository e Servizi base
    repository = InMemoryCounterRepository()
    blur_service = BlurService()
    zone_service = ZoneService()
    person_service = PersonService()
    
    # 2. Collegamento Observer → CountService ascolta il PersonService
    count_service = CountService()
    person_service.addListener(count_service)
    
    # 3. Setup del ReIDService
    # similarity_threshold=0.6 → soglia di default, puoi alzarla per essere più restrittivo
    reid_service = ReIDService(similarity_threshold=0.6, max_lost_seconds=30.0)
    
    # 4. Creazione MainService con TUTTE le dipendenze (incluso Re-ID)
    main_service = MainService(
        repository=repository,
        blur_service=blur_service,
        zone_service=zone_service,
        person_service=person_service,
        reid_service=reid_service,
        camera_id="cam_webcam"  # Identifica questa sorgente video
    )
    
    print("\nSetup completato. Apertura webcam...")
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Errore: Impossibile aprire la webcam.")
        return
    
    print("✅ Webcam aperta!")
    print("   Vedrai due etichette per ogni persona:")
    print("   - ID verde  = ID locale YOLO (tracking intra-camera)")
    print("   - GID arancione = ID globale Re-ID (cross-camera)")
    print("   Premi 'q' per uscire.\n")

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Il MainService ora orchestra tutto: zone → detection → re-id → blur
        processed_frame = main_service.process_frame(frame)
        
        cv2.imshow("Test Re-ID - MainService Completo", processed_frame)
        
        # Ogni 60 frame (~2 secondi), stampa le persone attive nel registro Re-ID
        frame_count += 1
        if frame_count % 60 == 0:
            active = reid_service.get_active_persons()
            if active:
                print(f"[Frame {frame_count}] Persone attive nel registro Re-ID: {len(active)}")
                for gid, info in active.items():
                    print(f"  → GID {gid} | Camera: {info['camera_id']}")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    print("\n--- Risultato finale ---")
    print(f"Persone uniche tracciate dal Re-ID: {reid_service._next_global_id - 1}")

if __name__ == "__main__":
    main()
