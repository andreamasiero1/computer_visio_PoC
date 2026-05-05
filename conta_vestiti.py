import cv2
from ultralytics import YOLO
from collections import defaultdict

MODELLO = 'yolov8m.pt'  # Modello pre-addestrato per rilevamento generico
SOGLIA_ALLERTA = 4

modello_persone = YOLO("yolov8n.pt")   # rileva persone (COCO)
modello_vestiti = YOLO("best.pt")

def get_boxes(results, nomi_target=None):
    trovati = []
    for box in results.boxes:
        nome=results.names[int(box.cls[0])]
        if nomi_target is None or nome in nomi_target:
            trovati.append({
                "classe": nome,
                "coords": box.xyxy[0].tolist(),
                "conf": float(box.conf[0])
            })
    return trovati

def capo_appartiene_a_persona(capo_coords, persona_coords):
    px1, py1, px2, py2 = persona_coords
    cx1, cy1, cx2, cy2 = capo_coords

    # Centro del capo
    cx = (cx1 + cx2) / 2
    cy = (cy1 + cy2) / 2

    # Allarga il box persona del 20% per includere capi tenuti in mano
    larghezza = px2 - px1
    altezza = py2 - py1
    margine_x = larghezza * 0.2
    margine_y = altezza * 0.2

    return (
        (px1 - margine_x) < cx < (px2 + margine_x) and
        (py1 - margine_y) < cy < (py2 + margine_y)
    )


def analizza_frame(frame):
    res_persone = modello_persone(frame, verbose=False)[0]
    res_vestiti = modello_vestiti(frame, verbose=False)[0]

    persone=get_boxes(res_persone, nomi_target=['person'])
    vestiti=get_boxes(res_vestiti)

    conteggio = {i: [] for i in range(len(persone))}

    for vestito in vestiti:
        for i, persona in enumerate(persone):
            if capo_appartiene_a_persona(vestito['coords'], persona['coords']):
                conteggio[i].append(vestito['classe'])
                break

    return persone, vestiti, conteggio

def disegna_risultati(frame, persone, conteggio):
    for i, persona in enumerate(persone):
        x1, y1, x2, y2 = map(int, persona['coords']) 
        capi=conteggio[i] 
        n_capi=len(capi)

        colore = (0, 255, 0) if n_capi <= SOGLIA_ALLERTA else (0, 0, 255)

        cv2.rectangle(frame, (x1, y1), (x2, y2), colore, 2)
        cv2.putText(frame, f'{n_capi} capi', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colore, 2)
        for j, capo in enumerate(capi):
            cv2.putText(frame, f"  - {capo}",
                        (x1, y2 + 20 + j * 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 0), 1)
        if n_capi > SOGLIA_ALLERTA:
            cv2.putText(frame, 'ALLERTA', (x1, y2 + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    return frame

def avvia(sorgente=0):
    """
    sorgente=0 → webcam del Mac
    sorgente="video.mp4" → file video
    """
    cap = cv2.VideoCapture(sorgente)
    
    print("PoC avviato. Premi 'Q' per uscire.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        persone, vestiti, conteggio = analizza_frame(frame)
        frame = disegna_risultati(frame, persone, conteggio)
        
        # Mostra statistiche in alto
        cv2.putText(frame, f"Persone rilevate: {len(persone)}",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, f"Capi totali: {len(vestiti)}",
                    (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        cv2.imshow("Clothing PoC", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


# Avvia con la webcam
avvia(0)
