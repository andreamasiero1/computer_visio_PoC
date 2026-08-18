---
title: "Edge AI"
type: concept
created: 2026-07-18
updated: 2026-08-19
tags: [edge-ai, edge-computing, inferenza-locale, privacy, latenza, architettura, cascade-funnel]
domain: "AI / Infrastruttura"
complexity: intermediate
confidence: high
related: ["[[pytorch]]", "[[distributed-data-parallel]]", "[[action-recognition]]", "[[object-counting]]", "[[computer-vision-retail-security]]", "[[cascade-funnel-pipeline]]", "[[capo-vivo]]", "[[logica-booleana-allarme]]"]
---

# 🧩 Edge AI

> Paradigma in cui i modelli di intelligenza artificiale vengono eseguiti localmente su dispositivi edge (server on-premise, dispositivi IoT) anziché nel cloud.

---

## Definizione

**Edge AI** è l'esecuzione di algoritmi di intelligenza artificiale direttamente sul dispositivo o sulla rete locale dove i dati vengono generati, eliminando la necessità di inviarli al cloud per il processing. Nel contesto del progetto VisAi, questo significa installare un **server fisico proprietario** all'interno di ogni punto vendita per processare i flussi video localmente.

---

## Vantaggi

| Vantaggio | Dettaglio |
|-----------|-----------|
| **Latenza zero** | Nessun round-trip verso il cloud — risposte in tempo reale |
| **Privacy by design** | I dati (video) non lasciano mai il punto vendita |
| **Compliance semplificata** | GDPR, EU AI Act — i dati sensibili restano on-premise con Face Blurring preventivo |
| **Resilienza** | Funziona anche senza connessione internet |
| **Costi operativi** | Nessun costo cloud ricorrente per il processing (ma costo hardware upfront) |

---

## Sfide e Soluzioni Edge in VisAi

| Sfida Edge | Soluzione Architetturale VisAi |
|---|---|
| **Risorse limitate su GPU on-premise** | Architettura a imbuto ([[cascade-funnel-pipeline]]) che scarica oltre il 95% del calcolo su regole deterministiche e filtri leggeri. |
| **Overhead per Scene Understanding** | Mascheramento geometrico delle **Zone Morte** configurato da GUI, senza modelli AI per la segmentazione statica. |
| **Saturazione da Multi-Tracking** | Tracciamento dinamico limitato unicamente a pochi [[capo-vivo]] attivi. |
| **Compliance GDPR / EU AI Act** | Face Blurring applicato immediatamente all'ingresso del flusso video (Fase 1). |

---

## Edge AI nel progetto VisAi

Il progetto VisAi adotta un'architettura **Edge AI pura**:

- **Server fisico proprietario** in ogni negozio.
- **Pipeline a 5 fasi** ([[cascade-funnel-pipeline]]) con trigger condizionali.
- **Telecamere proprietarie** ottimizzate per il software.
- **Processing video locale** per action recognition e object counting.
- **Oscuramento volti immediato** per compliance EU AI Act.
- Nessun dato video inviato al cloud.

> "Installeremo un server fisico proprietario all'interno di ogni punto vendita per processare i video localmente, garantendo latenza zero e massima sicurezza del dato." [^1]

---

## Tecniche di ottimizzazione per Edge

- **Cascade Funnel Processing**: Filtrare a monte il 95%+ dei pixel con maschere statiche e soglie geometriche prima di eseguire reti complesse.
- **Model quantization**: Ridurre la precisione dei pesi (FP32 → INT8 / FP16) per velocizzare l'inferenza.
- **Pruning e Knowledge distillation**: Reti compatte per person detection e pose estimation.
- **TensorRT / ONNX Runtime**: Ottimizzazione del grafo di inferenza su GPU locali.

---

## Fonti

- [[visai-progetto-readme]] — Architettura Edge AI del progetto VisAi
- [[architettura-flusso-sequenziale]] — Principi di ottimizzazione Edge e Cascade Funnel

[^1]: Fonte: [[visai-progetto-readme]]

---

*Ultimo aggiornamento: 2026-08-19 — Ingestione di [[architettura-flusso-sequenziale]]*
