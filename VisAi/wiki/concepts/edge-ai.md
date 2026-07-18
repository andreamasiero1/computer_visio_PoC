---
title: "Edge AI"
type: concept
created: 2026-07-18
updated: 2026-07-18
tags: [edge-ai, edge-computing, inferenza-locale, privacy, latenza, architettura]
domain: "AI / Infrastruttura"
complexity: intermediate
confidence: high
related: ["[[pytorch]]", "[[distributed-data-parallel]]", "[[action-recognition]]", "[[object-counting]]", "[[computer-vision-retail-security]]"]
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
| **Compliance semplificata** | GDPR, EU AI Act — i dati sensibili restano on-premise |
| **Resilienza** | Funziona anche senza connessione internet |
| **Costi operativi** | Nessun costo cloud ricorrente per il processing (ma costo hardware upfront) |

---

## Sfide

| Sfida | Dettaglio |
|-------|-----------|
| **Risorse limitate** | Il server locale ha meno potenza di un data center cloud |
| **Ottimizzazione modelli** | Necessario ottimizzare i modelli per girare su hardware locale (quantizzazione, pruning, TensorRT, ONNX) |
| **Manutenzione distribuita** | Ogni punto vendita ha il suo server → gestione e aggiornamenti distribuiti |
| **Hardware upfront** | Costo iniziale per server + telecamere proprietarie |

---

## Edge AI nel progetto VisAi

Il progetto VisAi adotta un'architettura **Edge AI pura**:

- **Server fisico proprietario** in ogni negozio
- **Telecamere proprietarie** ottimizzate per il software
- **Processing video locale** per action recognition e object counting
- **Oscuramento volti on-the-edge** per compliance EU AI Act
- Nessun dato video inviato al cloud

> "Installeremo un server fisico proprietario all'interno di ogni punto vendita per processare i video localmente, garantendo latenza zero e massima sicurezza del dato." [^1]

---

## Tecniche di ottimizzazione per Edge

- **Model quantization**: ridurre la precisione dei pesi (FP32 → INT8) per velocizzare l'inferenza
- **Pruning**: rimuovere connessioni ridondanti dalla rete neurale
- **Knowledge distillation**: addestrare un modello piccolo (student) a imitare uno grande (teacher)
- **TensorRT / ONNX Runtime**: framework di ottimizzazione per inferenza su GPU NVIDIA
- **Batch processing**: elaborare più frame contemporaneamente per massimizzare il throughput

---

## Fonti

- [[visai-progetto-readme]] — Architettura Edge AI del progetto VisAi

[^1]: Fonte: [[visai-progetto-readme]]

---

*Pagina creata da ingestione di [[visai-progetto-readme]]*
