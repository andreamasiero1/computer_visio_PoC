---
title: "Action Recognition / Pose Estimation"
type: concept
created: 2026-07-18
updated: 2026-07-18
tags: [action-recognition, pose-estimation, computer-vision, anomaly-detection, deep-learning]
domain: "Computer Vision"
complexity: advanced
confidence: high
related: ["[[edge-ai]]", "[[object-counting]]", "[[pytorch]]", "[[tensor]]", "[[computer-vision-retail-security]]"]
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

## Applicazione nel progetto VisAi

La core feature #1 del progetto richiede il **rilevamento di anomalie comportamentali** finalizzate all'occultamento intenzionale di capi di abbigliamento.

### Sfide specifiche

| Sfida | Dettaglio |
|-------|-----------|
| **Zero falsi positivi** | Distinguere tra furto e gesti normali (mani in tasca, sistemare borsa) |
| **Occlusioni** | Il soggetto può essere parzialmente nascosto da scaffali, altri clienti |
| **Varietà di azioni** | L'occultamento può avvenire in modi molto diversi |
| **Real-time** | L'analisi deve avvenire in tempo reale su Edge AI |
| **Illuminazione variabile** | Condizioni di luce diverse nelle varie zone del negozio |

### Pipeline ipotizzata

```
Video stream → Person Detection → Pose Estimation → Skeleton Sequence
    → Action Classification → Anomaly Score → Alert (se sopra soglia)
```

> "Rilevamento di anomalie comportamentali e atteggiamenti sospetti finalizzati all'occultamento intenzionale del capo [...] riducendo a zero i falsi positivi." [^1]

---

## Connessione con altri concetti

- Richiede [[tensor]] per la rappresentazione dei dati video
- Implementabile con [[pytorch]] (framework principale)
- Deve girare in architettura [[edge-ai]] (inferenza locale)
- Si integra con [[object-counting]] per la seconda core feature

---

## Fonti

- [[visai-progetto-readme]] — Core feature #1 del progetto

[^1]: Fonte: [[visai-progetto-readme]]

---

*Pagina creata da ingestione di [[visai-progetto-readme]]*
