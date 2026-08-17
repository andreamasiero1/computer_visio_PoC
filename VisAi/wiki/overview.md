---
title: "Overview — VisAi"
type: meta
created: 2026-07-18
updated: 2026-07-27
tags: [overview, meta]
---

# 🧠 VisAi — Panoramica

> Knowledge base personale di Andrea Masiero, costruita e mantenuta da un LLM.

---

## Stato attuale

| Metrica | Valore |
|---------|--------|
| Fonti ingerite | 3 + analisi business |
| Pagine wiki | 23 (index, log, overview, 3 sources, 2 entities, 12 concepts, 2 topics) |
| Entità tracciate | 2 (Sebastian Raschka, PyTorch) |
| Concetti mappati | 12 (8 tecnici + 4 business/strategy) |
| Topic attivi | 2 (Deep Learning & NLP, Computer Vision Retail Security) |
| Analisi generate | 0 |
| Ultima ingestione | 2026-07-27 — Analisi Business, Revenue Models, Product Strategy, Competitor Analysis |
| Ultima manutenzione (lint) | — |

---

## Temi principali

### 🤖 Deep Learning & NLP
La wiki copre sia la **teoria** (architettura Transformer, self-attention) sia la **pratica** (PyTorch, tensori, autograd, training loop, GPU computing, DDP). Le due fonti si complementano: il paper "Attention Is All You Need" spiega *cosa* sono i modelli moderni, il tutorial PyTorch spiega *come* implementarli.

### 🛡️ Computer Vision per la Sicurezza Retail
Progetto VisAi: startup che mira a sostituire i sistemi antitaccheggio fisici con computer vision ed Edge AI. Due core feature: **action recognition** per rilevare occultamento merce e **object counting** per monitorare i camerini. Architettura Edge AI pura con hardware proprietario.

### 💼 Business & Strategy (NUOVO)
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
```

---

## Due domini, una rete

La knowledge base ha **tre domini interconnessi**:
1. **Fondamenti teorici e pratici del deep learning** (Transformer, PyTorch, tensori, autograd)
2. **Applicazione concreta nel retail** (computer vision, Edge AI, action recognition, object counting)
3. **Business & Strategy** (shrinkage, revenue models, competitor analysis, product strategy)

I domini 1 e 2 sono tecnici. Il dominio 3 valida e guida le decisioni di prodotto.

---

## Evoluzione recente

- **2026-07-18 00:55**: Inizializzazione della wiki + prima ingestione (Attention Is All You Need)
- **2026-07-18 10:52**: Seconda ingestione (PyTorch in One Hour) — +1 source, +2 entities, +3 concepts
- **2026-07-18 11:10**: Terza ingestione (README Progetto VisAi) — +1 source, +3 concepts, +1 topic (nuovo dominio!)
- **2026-07-27 12:00**: Quarta ingestione (Analisi Business) — +4 concepts (retail-shrinkage, revenue-models-visai, product-strategy-lean-vs-full, competitor-analysis-loss-prevention). Decisioni strategiche chiave prese: target validato, revenue model definito, Lean approach approvato.

---

## Prossimi passi suggeriti

1. 📥 **Approfondisci Action Recognition**: ingerisci paper su SlowFast, PoseC3D, o VideoMAE per modelli video
2. 📥 **Approfondisci Object Detection**: ingerisci documentazione su YOLO, DETR per object counting
3. 📥 **Edge AI deployment**: articoli su TensorRT, ONNX, model quantization per ottimizzare l'inferenza
4. 📥 **Compliance**: documenti su GDPR, EU AI Act applicati alla video sorveglianza
5. 🔍 **Prova una query**: "quali modelli di action recognition funzionano meglio su Edge AI?"
6. 📋 **Roadmap tecnica Fase 1**: pipeline AI, architettura, milestone per il PoC
7. 💼 **Pitch deck**: creare il deck per investitori basato su analisi business
8. 🧹 **Primo lint**: la wiki ha 23 pagine — un health-check è consigliato
