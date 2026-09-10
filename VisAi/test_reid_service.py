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
    print("TEST INTEGRATO - Tutti i servizi")
    print("=" * 50)
    
    # 1. Setup Repository e Servizi base
    repository = InMemoryCounterRepository()
    blur_service = BlurService()
    zone_service = ZoneService()
    person_service = PersonService()
    
    # 2. CountService con line crossing
    count_service = CountService()
    person_service.addListener(count_service)
    
    # 3. ReIDService
    reid_service = ReIDService(similarity_threshold=0.6, max_lost_seconds=30.0)
    
    # 4. MainService con TUTTE le dipendenze
    main_service = MainService(
        repository=repository,
        blur_service=blur_service,
        zone_service=zone_service,
        person_service=person_service,
        reid_service=reid_service,
        camera_id="cam_webcam"
    )
    
    # 5. Apri la webcam e leggi le dimensioni
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Errore: Impossibile aprire la webcam.")
        return
    
    ret, first_frame = cap.read()
    if not ret:
        print("Errore lettura primo frame.")
        return
    
    frame_h, frame_w = first_frame.shape[:2]
    
    # 6. Imposta la linea di conteggio a metà schermo (verticale)
    line_x = frame_w // 2
    count_service.set_counting_lines([
        {
            "name": "linea_centrale",
            "orientation": "vertical",
            "position": line_x,
            "in_direction": "right"
        }
    ])
    
    print(f"\n✅ Setup completato ({frame_w}x{frame_h})!")
    print(f"   Servizi attivi: PersonService, CountService, ReIDService, BlurService")
    print(f"   Linea di conteggio a y={line_x}")
    print(f"   Premi 'q' per uscire.\n")

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Il MainService orchestra: zone → detection → re-id → blur
        processed_frame = main_service.process_frame(frame)
        
        # Disegna la linea di conteggio (rossa)
        cv2.line(processed_frame, (line_x, 0), (line_x, frame_h), (0, 0, 255), 3)
        
        # Mostra i contatori IN / OUT / Dentro
        counts = count_service.get_counts()
        cv2.putText(processed_frame, f"IN: {counts['in']}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        cv2.putText(processed_frame, f"OUT: {counts['out']}", (10, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
        cv2.putText(processed_frame, f"Dentro: {counts['currently_inside']}", (10, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 200, 0), 3)
        
        cv2.imshow("Test Integrato - Tutti i servizi", processed_frame)
        
        # Log periodico Re-ID
        frame_count += 1
        if frame_count % 120 == 0:
            active = reid_service.get_active_persons()
            if active:
                print(f"[Frame {frame_count}] Re-ID: {len(active)} persone attive | "
                      f"Conteggio: IN={counts['in']} OUT={counts['out']}")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    # Riepilogo finale
    print("\n" + "=" * 50)
    print("RIEPILOGO FINALE")
    print("=" * 50)
    counts = count_service.get_counts()
    print(f"Ingressi:          {counts['in']}")
    print(f"Uscite:            {counts['out']}")
    print(f"Persone dentro:    {counts['currently_inside']}")
    print(f"Persone uniche (Re-ID): {reid_service._next_global_id - 1}")
    
    log = count_service.get_events_log()
    if log:
        print(f"\nStorico eventi ({len(log)}):")
        for e in log:
            print(f"  {e['type']} | Persona {e['person_id']} | Linea: {e['line']}")

if __name__ == "__main__":
    main()

