---
title: "Overview — VisAi"
type: meta
created: 2026-07-18
updated: 2026-08-19
tags: [overview, meta]
---

# 🧠 VisAi — Panoramica

> Knowledge base personale di Andrea Masiero, costruita e mantenuta da un LLM.

---

## Stato attuale

| Metrica | Valore |
|---------|--------|
| Fonti ingerite | 4 + analisi business |
| Pagine wiki | 27 (index, log, overview, 4 sources, 2 entities, 15 concepts, 2 topics) |
| Entità tracciate | 2 (Sebastian Raschka, PyTorch) |
| Concetti mappati | 15 (11 tecnici + 4 business/strategy) |
| Topic attivi | 2 (Deep Learning & NLP, Computer Vision Retail Security) |
| Analisi generate | 0 |
| Ultima ingestione | 2026-08-19 — Architettura e Logica del Flusso Sequenziale (VisAi) |
| Ultima manutenzione (lint) | — |

---

## Temi principali

### 🤖 Deep Learning & NLP
La wiki copre sia la **teoria** (architettura Transformer, self-attention) sia la **pratica** (PyTorch, tensori, autograd, training loop, GPU computing, DDP). Le due fonti si complementano: il paper "Attention Is All You Need" spiega *cosa* sono i modelli moderni, il tutorial PyTorch spiega *come* implementarli.

### 🛡️ Computer Vision per la Sicurezza Retail
Progetto VisAi: startup che mira a sostituire i sistemi antitaccheggio fisici con computer vision ed Edge AI.
- **[[cascade-funnel-pipeline]]**: Architettura a imbuto a 5 fasi che riduce del 95%+ il carico computazionale.
- **[[capo-vivo]]**: Tracciamento dinamico e selettivo limitato ai capi prelevati da zone morte e conformi a soglie dimensionali/valore (€40-50+).
- **[[logica-booleana-allarme]]**: Decision logic a 3 fattori con timer di validazione a 10s per tollerare occlusioni legittime.
- **[[action-recognition]]**: Pose estimation e cinematica attive solo sull'intersezione persona-capo vivo.
- **[[object-counting]]**: Monitoraggio varchi camerini senza riprese interne.

### 💼 Business & Strategy
Analisi di mercato approfondita per la startup VisAi:
- **[[retail-shrinkage]]** — Differenze inventariali: OVS perde €8-10M/anno, Mango €12-15M/anno in furti esterni
- **[[revenue-models-visai]]** — Due modelli: SaaS (€290-690/mese) e Pay-per-Prevention (€75/furto)
- **[[product-strategy-lean-vs-full]]** — Decisione fondamentale: telecamere esistenti (Lean) vs copertura 360° (Full). Casi studio: Amazon JWO (fallito), Veesion ($27M ARR, scalato), Standard Cognition ($200M → pivot). Decisione: **Lean ora → Full come evoluzione**
- **[[competitor-analysis-loss-prevention]]** — Veesion è il competitor diretto (5.000 negozi, Series B $43M). Moat VisAi: privacy/compliance

---

## Connessioni chiave

```
Attention Is All You Need (2017)
    ├── introduce → Transformer
    │       ├── basato su → Self-Attention
    │       └── fondamento di → BERT, GPT, T5, PaLM, LLaMA...
    └── topic → Deep Learning & NLP

PyTorch in One Hour (2025) — Sebastian Raschka
    ├── introduce → Tensor, Autograd, DDP
    ├── strumento → PyTorch
    └── topic → Deep Learning & NLP

README Progetto VisAi (2026) — Andrea Masiero
    ├── introduce → Edge AI, Action Recognition, Object Counting
    ├── usa → PyTorch (per implementare i modelli)
    ├── topic → Computer Vision Retail Security
    └── connessione → Tensor, Autograd (per training modelli CV)

Analisi Business (2026-07-27) — Andrea Masiero + Antigravity
    ├── introduce → Retail Shrinkage, Revenue Models, Product Strategy, Competitor Analysis
    ├── valida → Target mercato (OVS, Mango)
    ├── decide → Lean approach → Full Revolution (fasi)
    ├── benchmark → Veesion, Amazon JWO, Standard AI
    └── topic → Computer Vision Retail Security (business side)

Architettura Flusso Sequenziale (2026-08-19) — Andrea Masiero
    ├── formalizza → Cascade Funnel Pipeline (5 Fasi)
    ├── introduce → Capo Vivo, Logica Booleana Allarme (timer 10s)
    ├── integra → Zone Morte GUI, Face Blurring immediato (GDPR/EU AI Act)
    └── ottimizza → Edge AI, Action Recognition selettivo
```

---

## Tre domini, una rete

La knowledge base ha **tre domini interconnessi**:
1. **Fondamenti teorici e pratici del deep learning** (Transformer, PyTorch, tensori, autograd)
2. **Applicazione concreta nel retail** (computer vision, Edge AI, cascade funnel, action recognition, object counting)
3. **Business & Strategy** (shrinkage, revenue models, competitor analysis, product strategy)

---

## Evoluzione recente

- **2026-07-18 00:55**: Inizializzazione della wiki + prima ingestione (Attention Is All You Need)
- **2026-07-18 10:52**: Seconda ingestione (PyTorch in One Hour) — +1 source, +2 entities, +3 concepts
- **2026-07-18 11:10**: Terza ingestione (README Progetto VisAi) — +1 source, +3 concepts, +1 topic (nuovo dominio!)
- **2026-07-27 12:00**: Quarta ingestione (Analisi Business) — +4 concepts. Decisioni strategiche chiave approvate.
- **2026-08-19 01:45**: Quinta ingestione (Architettura e Logica del Flusso Sequenziale) — +1 source, +3 concepts (cascade-funnel-pipeline, capo-vivo, logica-booleana-allarme), +2 concepts aggiornati (action-recognition, edge-ai), +1 topic aggiornato.

---

## Prossimi passi suggeriti

1. 📥 **Approfondisci Action Recognition**: ingerisci paper su SlowFast, PoseC3D, o VideoMAE per modelli video
2. 📥 **Approfondisci Object Detection**: ingerisci documentazione su YOLO, DETR per object counting
3. 📥 **Edge AI deployment**: articoli su TensorRT, ONNX, model quantization per ottimizzare l'inferenza
4. 📥 **Compliance**: documenti su GDPR, EU AI Act applicati alla video sorveglianza
5. 🔍 **Prova una query**: "come interagiscono Capo Vivo e Action Recognition nel Cascade Funnel?"
6. 📋 **Roadmap tecnica Fase 1**: pipeline AI, architettura, milestone per il PoC
7. 💼 **Pitch deck**: creare il deck per investitori basato su analisi business
8. 🧹 **Primo lint**: la wiki ha 27 pagine — un health-check è consigliato
