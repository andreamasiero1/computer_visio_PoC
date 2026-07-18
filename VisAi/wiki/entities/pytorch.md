---
title: "PyTorch"
type: entity
entity_type: tool
created: 2026-07-18
updated: 2026-07-18
tags: [pytorch, framework, deep-learning, python, open-source]
aliases: ["torch", "PyTorch"]
confidence: high
related: ["[[tensor]]", "[[autograd]]", "[[distributed-data-parallel]]", "[[transformer]]", "[[sebastian-raschka]]", "[[deep-learning-nlp]]"]
---

# 🔧 PyTorch

> Libreria open-source Python per il deep learning, la più usata nella ricerca accademica dal 2019.

---

## Definizione

**PyTorch** è una libreria open-source per il deep learning basata su Python. Originariamente sviluppata da Meta AI (Facebook AI Research), è diventata il framework di riferimento per la ricerca e sempre più per la produzione. Il nome "PyTorch" deriva da "Torch", un framework scientifico originariamente scritto in Lua.

---

## Tre componenti core

| Componente | Descrizione |
|------------|-------------|
| **Tensor Library** | Libreria di array multidimensionali simile a NumPy, con supporto nativo per GPU (CUDA) e Apple Silicon (MPS) |
| **Autograd Engine** | Motore di differenziazione automatica che costruisce grafi computazionali e calcola gradienti via `loss.backward()` |
| **Deep Learning Utilities** | Moduli per costruire reti neurali (`torch.nn`), ottimizzatori (`torch.optim`), data loading (`DataLoader`), loss functions |

---

## Caratteristiche chiave

- **API NumPy-like**: sintassi familiare per chi conosce NumPy
- **Dynamic computation graphs**: il grafo viene costruito on-the-fly (eager execution), facilitando debug e sperimentazione
- **GPU computing semplice**: basta `.to("cuda")` per spostare tensori/modelli su GPU
- **Multi-GPU con DDP**: `DistributedDataParallel` per training distribuito su più GPU
- **Default float32**: bilancia precisione ed efficienza computazionale
- **Ecosistema ricco**: torchvision, torchaudio, torchtext, Hugging Face Transformers

---

## Adozione

- Libreria di deep learning **più usata nella ricerca** dal 2019 (Papers With Code) [^1]
- ~40% dei rispondenti al Kaggle Survey 2022 la utilizzano, con crescita annuale costante [^1]
- Usata per implementare la maggior parte degli LLM moderni (GPT, LLaMA, etc.)

---

## Installazione

```bash
pip install torch          # installazione base (auto-detecta GPU)
pip install torch==2.4.1   # versione specifica
```

Per Apple Silicon: `torch.backends.mps.is_available()` verifica il supporto.

---

## Fonti

- [[pytorch-in-one-hour]] — Tutorial completo di [[sebastian-raschka]]

[^1]: Fonte: [[pytorch-in-one-hour]] — Sebastian Raschka, 2025

---

*Pagina creata da ingestione di [[pytorch-in-one-hour]]*
