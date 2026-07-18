---
title: "Object Counting / Re-Identification"
type: concept
created: 2026-07-18
updated: 2026-07-18
tags: [object-counting, re-identification, tracking, computer-vision, camerini, deep-learning]
domain: "Computer Vision"
complexity: advanced
confidence: high
related: ["[[edge-ai]]", "[[action-recognition]]", "[[pytorch]]", "[[computer-vision-retail-security]]"]
---

# 🧩 Object Counting / Re-Identification

> Tecniche di computer vision per contare e ri-identificare oggetti attraverso frame video successivi. Nel contesto VisAi, usate per monitorare i capi in entrata/uscita dai camerini.

---

## Definizione

### Object Counting
L'**Object Counting** è il task di contare il numero di istanze di un determinato tipo di oggetto in un'immagine o attraverso un flusso video. Può essere:
- **Detection-based**: prima si individuano gli oggetti, poi si contano
- **Density-based**: si stima una mappa di densità e si integra per ottenere il conteggio
- **Counting by tracking**: si tracciano gli oggetti attraverso i frame e si contano quelli che attraversano una linea/zona

### Re-Identification (ReID)
La **Re-Identification** è il task di riconoscere la stessa entità (persona o oggetto) attraverso diverse viste, telecamere o momenti temporali. Nel contesto VisAi, si applica ai **capi di abbigliamento** portati dentro e fuori dai camerini.

---

## Approcci principali

### Object Counting

| Approccio | Descrizione | Uso |
|-----------|-------------|-----|
| **Detection + Counting** | YOLO/DETR per detect, poi conta | Oggetti ben definiti |
| **Line crossing** | Conta oggetti che attraversano una linea virtuale | Entrate/uscite |
| **Density estimation** | Mappa di densità (CSRNet, etc.) | Folle, oggetti piccoli |

### Re-Identification

| Approccio | Descrizione | Uso |
|-----------|-------------|-----|
| **Appearance-based** | Embedding visuale per matching | ReID persone/oggetti |
| **Metric learning** | Triplet loss, contrastive learning | Similarità tra capi |
| **Multi-Object Tracking** | Tracking continuo con ID assegnato | Video in tempo reale |

---

## Applicazione nel progetto VisAi

La core feature #2 del progetto richiede il **monitoraggio dei capi in entrata/uscita dai camerini**.

### Logica operativa

```
Telecamera dedicata all'ingresso camerino
    ↓
Person Detection → Tracking
    ↓
Object Detection (capi in mano/braccio)
    ↓
Count IN (entrata) → Count OUT (uscita)
    ↓
Δ = IN - OUT → Se Δ > 0: ALERT (capo mancante)
```

### Sfide specifiche

| Sfida | Dettaglio |
|-------|-----------|
| **Privacy camerino** | Non si può filmare l'interno del camerino — solo entrata/uscita |
| **Occlusioni** | I capi possono essere piegati, sovrapposti, in borse |
| **Variabilità dei capi** | Colori, dimensioni, textures molto diverse |
| **Capi indossati** | Il cliente può indossare un capo sotto i propri vestiti |
| **Più clienti** | Gestire più persone che entrano/escono contemporaneamente |
| **Real-time** | Deve funzionare in tempo reale su Edge AI |

### Vincolo di privacy

> "Come tracciare gli oggetti in mano al cliente (entrata vs uscita) senza violare la privacy visiva dell'interno del camerino." [^1]

Questo vincolo architetturale impone che il sistema lavori **esclusivamente sulle immagini di entrata e uscita**, senza accesso all'interno del camerino.

---

## Connessione con altri concetti

- Si integra con [[action-recognition]] per una detection multi-layer
- Gira su architettura [[edge-ai]] (inferenza locale)
- Implementabile con [[pytorch]]
- Richiede [[tensor]] per la rappresentazione dei dati

---

## Fonti

- [[visai-progetto-readme]] — Core feature #2 del progetto

[^1]: Fonte: [[visai-progetto-readme]]

---

*Pagina creata da ingestione di [[visai-progetto-readme]]*
