---
title: "Action Recognition / Pose Estimation"
type: concept
created: 2026-07-18
updated: 2026-08-19
tags: [action-recognition, pose-estimation, computer-vision, anomaly-detection, deep-learning, capo-vivo, cascade-funnel]
domain: "Computer Vision"
complexity: advanced
confidence: high
related: ["[[edge-ai]]", "[[object-counting]]", "[[pytorch]]", "[[tensor]]", "[[computer-vision-retail-security]]", "[[cascade-funnel-pipeline]]", "[[capo-vivo]]", "[[logica-booleana-allarme]]"]
---

# 🧩 Action Recognition / Pose Estimation

> Tecniche di computer vision per riconoscere azioni umane e stimare la posa del corpo da video. Nel contesto VisAi, usate per rilevare comportamenti sospetti di occultamento merce.

---

## Definizione

### Action Recognition
L'**Action Recognition** è il task di computer vision che consiste nel riconoscere e classificare le azioni compiute da una o più persone in un video. Combina l'analisi spaziale (cosa si vede in un singolo frame) con l'analisi temporale (come la scena evolve nel tempo).

### Pose Estimation
La **Pose Estimation** è il task di individuare le articolazioni chiave (keypoints) del corpo umano in un'immagine o video — testa, spalle, gomiti, polsi, anche, ginocchia, caviglie — e connetterle per ricostruire lo scheletro della persona.

---

## Approcci principali

### Action Recognition

| Approccio | Descrizione | Esempi |
|-----------|-------------|--------|
| **3D CNN** | Convoluzioni su volume spazio-temporale | C3D, I3D, SlowFast |
| **Two-Stream** | Due reti: una per RGB, una per optical flow | Two-Stream CNN |
| **Skeleton-based** | Analisi dello scheletro (keypoints) nel tempo | ST-GCN, PoseC3D |
| **Video Transformer** | Attention su patch spazio-temporali | ViViT, TimeSformer, VideoMAE |

### Pose Estimation

| Approccio | Descrizione | Esempi |
|-----------|-------------|--------|
| **Top-down** | Prima detect la persona, poi stima la posa | HRNet, ViTPose |
| **Bottom-up** | Prima trova tutti i keypoints, poi li raggruppa | OpenPose, DEKR |

---

## Applicazione nel progetto VisAi (Cascade Funnel — Fase 4)

La core feature #1 del progetto richiede il **rilevamento di anomalie comportamentali** finalizzate all'occultamento intenzionale di capi di abbigliamento.

Nel modello operativo a imbuto ([[cascade-funnel-pipeline]]), i moduli pesanti di Action Recognition e Pose Estimation **non girano continuamente su tutto il frame**, ma si attivano **esclusivamente quando viene identificato un [[capo-vivo]]**:

1. **Trigger mirato**: Si analizza unicamente l'intersezione geometrica/spaziale tra la bounding box della Persona (Fase 2) e il Capo Vivo (Fase 3).
2. **Analisi Cinematica**: Rilevamento di traiettorie anomale degli arti (es. braccio che infila il capo all'interno di una giacca, in uno zaino o sotto un indumento personale).
3. **Validazione Temporale Sequenziale**: Se scatta il flag di gesto sospetto, la decisione finale è delegata al timer di 10s ([[logica-booleana-allarme]]) per azzerare i falsi positivi da occlusione.

### Pipeline Operativa VisAi

```
Video Stream (Fase 1: Face Blur + Mask Zone Morte)
    │
    ▼ (Fase 2: Person Detection)
Coordinate Persone
    │
    ▼ (Fase 3: Transizione Capo da Zona Morta)
[ CAPO VIVO ]
    │
    ▼ (Fase 4: Pose Estimation + Action Recognition su ROI Intersezione)
Gesto Sospetto Rilevato
    │
    ▼ (Fase 5: Timer 10s Doppia Verifica)
Allarme Confermato
```

---

## Connessione con altri concetti

- Ottimizzato tramite [[cascade-funnel-pipeline]] per girare su architetture [[edge-ai]]
- Elabora unicamente oggetti promossi a [[capo-vivo]]
- Condizione abilitante per la [[logica-booleana-allarme]]
- Richiede [[tensor]] per i dati video e implementabile con [[pytorch]]
- Si integra con [[object-counting]] per il monitoraggio dei camerini

---

## Fonti

- [[visai-progetto-readme]] — Core feature #1 del progetto
- [[architettura-flusso-sequenziale]] — Flusso a 5 Fasi e trigger Fase 4

---

*Ultimo aggiornamento: 2026-08-19 — Ingestione di [[architettura-flusso-sequenziale]]*
