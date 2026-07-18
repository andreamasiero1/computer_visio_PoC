---
title: "Attention Is All You Need"
type: source
source_type: paper
created: 2026-07-18
updated: 2026-07-18
tags: [transformer, attention, deep-learning, nlp, architettura-neurale]
sources: ["raw/papers/attention-is-all-you-need.md"]
author: "Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin"
date_published: 2017-06-12
url: "https://arxiv.org/abs/1706.03762"
confidence: high
related: ["[[transformer]]", "[[self-attention]]", "[[architetture-neurali]]", "[[nlp]]"]
---

# 📄 Attention Is All You Need

> Paper fondativo che introduce l'architettura **Transformer**, eliminando ricorrenza e convoluzioni a favore di meccanismi di attenzione puri.

---

## Riassunto

Il paper propone il **Transformer**, un'architettura neurale per sequence transduction basata esclusivamente su meccanismi di **self-attention**. A differenza delle RNN (LSTM, GRU) che processano i token in sequenza, il Transformer processa l'intera sequenza in parallelo, risolvendo due problemi fondamentali: la **limitata parallelizzazione** e la **difficoltà nel catturare dipendenze a lungo raggio**.

L'architettura mantiene la struttura encoder-decoder classica, ma sostituisce i layer ricorrenti con stack di **Multi-Head Self-Attention** e **Feed-Forward Networks**. L'informazione posizionale, persa eliminando la ricorrenza, viene reintrodotta tramite **Positional Encoding** sinusoidali.

I risultati sono eccezionali: il Transformer raggiunge un nuovo stato dell'arte sulla traduzione EN→DE (28.4 BLEU, +2 sopra il miglior ensemble) e EN→FR (41.8 BLEU), con un costo di training drasticamente inferiore — 3.5 giorni su 8 GPU rispetto a settimane per i modelli precedenti.

---

## Key Takeaways

1. 🏗️ **Architettura rivoluzionaria**: il Transformer elimina completamente ricorrenza e convoluzioni, basandosi solo su attenzione
2. ⚡ **Parallelizzazione**: processare tutti i token simultaneamente permette training molto più veloce
3. 🔗 **Dipendenze a lungo raggio**: la self-attention connette direttamente qualsiasi coppia di posizioni (path length O(1) vs O(n) delle RNN)
4. 🎯 **Multi-Head Attention**: multiple teste di attenzione catturano aspetti diversi delle relazioni tra token
5. 📈 **Impatto storico**: è diventato il fondamento di tutti gli LLM moderni (BERT, GPT, T5, PaLM, LLaMA)

---

## Componenti tecnici chiave

| Componente | Funzione |
|-----------|----------|
| Scaled Dot-Product Attention | `softmax(QK^T / √d_k) V` — meccanismo base |
| Multi-Head Attention | N teste parallele che catturano aspetti diversi |
| Positional Encoding | Sinusoidi per iniettare informazione posizionale |
| Encoder Stack | 6 layer identici (self-attention + FFN) |
| Decoder Stack | 6 layer con masked self-attention + cross-attention + FFN |
| Feed-Forward Network | Rete posizione per posizione, stessa per ogni posizione |

---

## Citazioni rilevanti

> "We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely."

> "Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU."

---

## Connessioni

- Introduce: [[transformer]], [[self-attention]], [[multi-head-attention]], [[positional-encoding]]
- Supera: RNN, LSTM, GRU per task di sequence transduction
- Fondamento di: [[bert]], [[gpt]], ogni LLM moderno
- Dominio: [[nlp]], [[deep-learning]], [[architetture-neurali]]

---

*Fonte: [attention-is-all-you-need.md](../raw/papers/attention-is-all-you-need.md)*
