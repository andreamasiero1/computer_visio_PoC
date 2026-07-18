---
title: "Transformer"
type: concept
created: 2026-07-18
updated: 2026-07-18
tags: [transformer, architettura-neurale, deep-learning, nlp]
domain: "Deep Learning / NLP"
complexity: intermediate
confidence: high
related: ["[[self-attention]]", "[[multi-head-attention]]", "[[positional-encoding]]", "[[nlp]]", "[[architetture-neurali]]", "[[pytorch]]", "[[tensor]]"]
---

# 🧩 Transformer

> Architettura neurale basata esclusivamente su meccanismi di attenzione, introdotta nel 2017. Fondamento di tutti i modelli di linguaggio moderni.

---

## Definizione

Il **Transformer** è un'architettura neurale per sequence transduction (trasformazione di sequenze) che sostituisce completamente la ricorrenza (RNN, LSTM, GRU) e le convoluzioni con meccanismi di **self-attention**. Introdotto nel paper [[attention-is-all-you-need]] (Vaswani et al., 2017).

---

## Caratteristiche chiave

- **Nessuna ricorrenza**: processa tutti i token in parallelo, non in sequenza
- **Self-Attention**: ogni token può "guardare" direttamente ogni altro token nella sequenza
- **Multi-Head**: multiple teste di attenzione catturano relazioni diverse
- **Positional Encoding**: l'informazione posizionale viene iniettata esplicitamente
- **Struttura modulare**: stack di layer identici (encoder e decoder)

---

## Architettura

```
Input → Embedding + Positional Encoding
    ↓
┌─ Encoder (×6) ─────────────────────┐
│  Multi-Head Self-Attention          │
│  Add & Norm                         │
│  Feed-Forward Network               │
│  Add & Norm                         │
└─────────────────────────────────────┘
    ↓
┌─ Decoder (×6) ─────────────────────┐
│  Masked Multi-Head Self-Attention   │
│  Add & Norm                         │
│  Multi-Head Cross-Attention         │
│  Add & Norm                         │
│  Feed-Forward Network               │
│  Add & Norm                         │
└─────────────────────────────────────┘
    ↓
Linear → Softmax → Output
```

---

## Perché è importante

Il Transformer ha risolto due limitazioni fondamentali delle RNN:

1. **Parallelizzazione**: le RNN processano token uno alla volta → training lento. Il Transformer processa tutto simultaneamente → training ordini di grandezza più veloce.
2. **Dipendenze a lungo raggio**: nelle RNN, l'informazione si degrada attraversando molti step. Nel Transformer, ogni token è connesso direttamente a ogni altro (path length O(1)).

---

## Discendenti

| Modello | Anno | Tipo | Note |
|---------|------|------|------|
| BERT | 2018 | Encoder-only | Bidirezionale, pre-training MLM |
| GPT | 2018 | Decoder-only | Autoregressive, scalato fino a GPT-4 |
| T5 | 2019 | Encoder-Decoder | "Text-to-Text" framework |
| PaLM | 2022 | Decoder-only | 540B parametri, Google |
| LLaMA | 2023 | Decoder-only | Open source, Meta |

---

## Fonti

- [[attention-is-all-you-need]] — Paper originale (Vaswani et al., 2017)
- [[pytorch-in-one-hour]] — Implementazione pratica di reti neurali (inclusi modelli basati su Transformer) in PyTorch

---

*Pagina creata da ingestione di [[attention-is-all-you-need]]*
