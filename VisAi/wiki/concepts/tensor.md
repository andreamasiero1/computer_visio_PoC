---
title: "Tensor"
type: concept
created: 2026-07-18
updated: 2026-07-18
tags: [tensor, struttura-dati, deep-learning, pytorch, numpy]
domain: "Deep Learning / Fondamenti"
complexity: basic
confidence: high
related: ["[[pytorch]]", "[[autograd]]", "[[transformer]]", "[[self-attention]]"]
---

# 🧩 Tensor

> Struttura dati fondamentale del deep learning che generalizza scalari, vettori e matrici a dimensioni arbitrarie.

---

## Definizione

Un **tensore** è un oggetto matematico che generalizza il concetto di vettore e matrice a dimensioni (rank) arbitrarie. In ambito computazionale, i tensori sono container di dati multidimensionali — la struttura fondamentale su cui operano tutte le reti neurali.

---

## Rank (Ordine)

| Rank | Nome | Esempio PyTorch | Forma |
|------|------|-----------------|-------|
| 0 | Scalare | `torch.tensor(1)` | `[]` |
| 1 | Vettore | `torch.tensor([1, 2, 3])` | `[3]` |
| 2 | Matrice | `torch.tensor([[1, 2], [3, 4]])` | `[2, 2]` |
| 3+ | Tensore nD | `torch.tensor([[[1,2],[3,4]],[[5,6],[7,8]]])` | `[2, 2, 2]` |

⚠️ **Nota**: un vettore 3D (3 elementi) è un tensore di rank 1, non rank 3. Il rank indica il numero di dimensioni, non il numero di elementi.

---

## Tipi di dato in PyTorch

| Tipo | Default per | Uso tipico |
|------|-------------|------------|
| `torch.int64` | Interi Python | Indici, label |
| `torch.float32` | Float Python | **Pesi dei modelli, training** (default) |
| `torch.float16` | — | Mixed precision training |
| `torch.bfloat16` | — | Training LLM (migliore range dinamico) |

Il default **float32** è una scelta di design: bilancia precisione e efficienza computazionale. Le GPU sono ottimizzate per operazioni a 32 bit [^1].

Conversione di tipo:
```python
tensor_float = tensor_int.to(torch.float32)
```

---

## Operazioni fondamentali

```python
import torch

t = torch.tensor([[1, 2, 3], [4, 5, 6]])

t.shape        # torch.Size([2, 3])
t.reshape(3,2) # Reshape
t.view(3, 2)   # Reshape (più comune in PyTorch)
t.T            # Trasposta
t @ t.T        # Moltiplicazione matriciale (equivale a t.matmul(t.T))
```

---

## Tensori vs NumPy Arrays

| Caratteristica | NumPy | PyTorch Tensors |
|---------------|-------|-----------------|
| API | Base | Simile a NumPy |
| GPU support | ❌ | ✅ (`.to("cuda")`) |
| Autograd | ❌ | ✅ (`requires_grad=True`) |
| Dynamic graphs | ❌ | ✅ |
| Default float | `float64` | `float32` |

---

## Fonti

- [[pytorch-in-one-hour]] — Sezioni 2.1-2.3 (Sebastian Raschka, 2025)

[^1]: Fonte: [[pytorch-in-one-hour]] — "32-bit floating point number offers sufficient precision for most deep learning tasks, while consuming less memory and computational resources"

---

*Pagina creata da ingestione di [[pytorch-in-one-hour]]*
