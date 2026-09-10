import cv2
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.services.person_service import PersonService
from src.services.count_service import CountService

def main():
    print("=" * 50)
    print("TEST CountService - Line Crossing")
    print("=" * 50)
    
    # 1. Setup servizi
    person_service = PersonService()
    count_service = CountService()
    person_service.addListener(count_service)
    
    # 2. Apri la webcam per leggere le dimensioni del frame
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Errore: Impossibile aprire la webcam.")
        return
    
    ret, first_frame = cap.read()
    if not ret:
        print("Errore lettura primo frame.")
        return
    
    frame_h, frame_w = first_frame.shape[:2]
    
    # 3. Imposta una linea di conteggio orizzontale a metà schermo
    # Se cammini dall'alto verso il basso → IN
    # Se cammini dal basso verso l'alto → OUT
    line_x = frame_w // 2
    count_service.set_counting_lines([
        {
            "name": "linea_centrale",
            "orientation": "vertical",
            "position": line_x,
            "in_direction": "right"
        }
    ])
    
    print(f"\n✅ Webcam aperta ({frame_w}x{frame_h})!")
    print(f"   Linea di conteggio orizzontale a y={line_x} (metà schermo).")
    print(f"   Attraversa la linea rossa muovendoti:")
    print(f"     ↓ dall'alto al basso = INGRESSO (🟢)")
    print(f"     ↑ dal basso all'alto = USCITA (🔴)")
    print(f"   Premi 'q' per uscire.\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detection + tracking (notifica automaticamente il CountService via Listener)
        processed_frame, detections = person_service.detectAndTrack(frame)
        
        # Disegna la linea di conteggio (rossa, spessa)
        cv2.line(processed_frame, (line_x, 0), (line_x, frame_h), (0, 0, 255), 3)
        cv2.putText(processed_frame, "LINEA DI CONTEGGIO", (10, line_x - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # Mostra i contatori in alto a sinistra
        counts = count_service.get_counts()
        cv2.putText(processed_frame, f"IN: {counts['in']}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        cv2.putText(processed_frame, f"OUT: {counts['out']}", (10, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
        cv2.putText(processed_frame, f"Dentro: {counts['currently_inside']}", (10, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 200, 0), 3)
        
        cv2.imshow("Test CountService - Line Crossing", processed_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    # Stampa riepilogo finale
    print("\n--- RIEPILOGO ---")
    counts = count_service.get_counts()
    print(f"Ingressi totali:  {counts['in']}")
    print(f"Uscite totali:    {counts['out']}")
    print(f"Persone dentro:   {counts['currently_inside']}")
    
    log = count_service.get_events_log()
    if log:
        print(f"\nStorico eventi ({len(log)} totali):")
        for e in log:
            print(f"  {e['type']} | Persona {e['person_id']} | Linea: {e['line']}")

if __name__ == "__main__":
    main()
