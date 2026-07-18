---
title: "Self-Attention"
type: concept
created: 2026-07-18
updated: 2026-07-18
tags: [self-attention, attention, transformer, deep-learning]
domain: "Deep Learning"
complexity: intermediate
confidence: high
related: ["[[transformer]]", "[[multi-head-attention]]", "[[attention-is-all-you-need]]"]
---

# 🧩 Self-Attention

> Meccanismo che permette a ogni elemento di una sequenza di "guardare" tutti gli altri elementi per calcolare la propria rappresentazione.

---

## Definizione

La **Self-Attention** (o intra-attention) è un meccanismo di attenzione in cui Query, Key e Value provengono tutti dalla stessa sequenza. Ogni token calcola un peso di attenzione rispetto a tutti gli altri token, creando una rappresentazione che è una media pesata di tutti i valori.

---

## Formula

```
Attention(Q, K, V) = softmax(QK^T / √d_k) · V
```

Dove:
- **Q** (Query): "cosa sto cercando?"
- **K** (Key): "cosa offro come corrispondenza?"
- **V** (Value): "quale informazione porto?"
- **√d_k**: fattore di scala per evitare gradienti troppo piccoli nel softmax

---

## Intuizione

Immagina una frase: *"Il gatto si sedette sul tappeto perché era stanco"*.

La self-attention permette alla parola "era" di "guardare indietro" e determinare che "era" si riferisce a "gatto" (non a "tappeto"), assegnando un peso di attenzione alto a "gatto".

---

## Vantaggi rispetto alla ricorrenza

| Proprietà | RNN | Self-Attention |
|-----------|-----|----------------|
| Path length tra posizioni | O(n) | O(1) |
| Parallelizzazione | No (sequenziale) | Sì (tutto in parallelo) |
| Complessità per layer | O(n · d²) | O(n² · d) |

⚠️ La complessità O(n²) della self-attention è il suo punto debole principale per sequenze molto lunghe — da qui nascono varianti come Sparse Attention, Linear Attention, etc.

---

## Fonti

- [[attention-is-all-you-need]] — Definizione formale nel paper Transformer

---

*Pagina creata da ingestione di [[attention-is-all-you-need]]*
