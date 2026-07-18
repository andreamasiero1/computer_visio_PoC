---
title: "Distributed Data Parallel (DDP)"
type: concept
created: 2026-07-18
updated: 2026-07-18
tags: [ddp, distributed-training, multi-gpu, pytorch, parallelismo, scalabilita]
domain: "Deep Learning / Infrastruttura"
complexity: advanced
confidence: high
related: ["[[pytorch]]", "[[autograd]]", "[[tensor]]", "[[deep-learning-nlp]]"]
---

# 🧩 Distributed Data Parallel (DDP)

> Strategia di PyTorch per il training distribuito su GPU multiple. Replica il modello su ogni GPU, divide i dati e sincronizza i gradienti.

---

## Definizione

**DistributedDataParallel (DDP)** è la strategia standard di PyTorch per accelerare il training distribuendo il lavoro su più GPU. Ogni GPU riceve una copia completa del modello e un sottoinsieme diverso dei dati. I gradienti vengono calcolati indipendentemente e poi sincronizzati tra le GPU per mantenere i modelli allineati.

---

## Come funziona

### Fase 1 — Setup

```
GPU 0: Copia del modello + Batch A
GPU 1: Copia del modello + Batch B
```

- Il modello viene replicato su ogni GPU
- Un `DistributedSampler` divide i dati in batch non sovrapposti

### Fase 2 — Forward + Backward (indipendente)

Ogni GPU esegue il proprio forward pass e backward pass in modo indipendente con il suo sottoinsieme di dati.

### Fase 3 — Sincronizzazione gradienti

I gradienti calcolati su ogni GPU vengono **mediati e sincronizzati** (all-reduce) tra tutte le GPU. Così ogni replica ha gli stessi gradienti e, dopo l'optimizer step, gli stessi pesi.

---

## Scalabilità

| GPU | Speedup teorico | Note |
|-----|-----------------|------|
| 1 | 1× (baseline) | Training standard |
| 2 | ~2× | Overhead minimo di comunicazione |
| 4 | ~4× | Scala quasi linearmente |
| 8 | ~8× | Richiede dataset abbastanza grande |

> "Barring a minor communication overhead between devices that comes with DDP use, it can theoretically process a training epoch in half the time with two GPUs." [^1]

---

## Implementazione (codice essenziale)

```python
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data.distributed import DistributedSampler
from torch.distributed import init_process_group, destroy_process_group

# Setup
init_process_group(backend="nccl")  # NCCL per GPU NVIDIA
torch.cuda.set_device(rank)

# Data loader con DistributedSampler
train_loader = DataLoader(
    dataset=train_ds,
    sampler=DistributedSampler(train_ds),  # divide i dati tra GPU
    shuffle=False,  # lo shuffle è gestito dal sampler
)

# Wrapping del modello
model = DDP(model.to(rank), device_ids=[rank])

# Training loop (quasi identico al single-GPU)
for features, labels in train_loader:
    features, labels = features.to(rank), labels.to(rank)
    # ... forward, loss, backward, step (come sempre)

# Cleanup
destroy_process_group()
```

### Lancio con torchrun

```bash
# Su 2 GPU
torchrun --nproc_per_node=2 script.py

# Su tutte le GPU disponibili
torchrun --nproc_per_node=$(nvidia-smi -L | wc -l) script.py
```

---

## Concetti chiave

| Termine | Significato |
|---------|-------------|
| **rank** | ID univoco del processo (= indice GPU) |
| **world_size** | Numero totale di processi/GPU |
| **NCCL** | NVIDIA Collective Communication Library (backend ottimizzato per GPU) |
| **gloo** | Backend alternativo (usato su Windows o senza GPU NVIDIA) |
| **DistributedSampler** | Divide il dataset tra i processi senza sovrapposizioni |
| **torchrun** | Utility di PyTorch che lancia automaticamente un processo per GPU |

---

## Limitazioni e alternative

- **DDP richiede che il modello intero stia in una singola GPU** — se il modello è troppo grande, usare **FSDP** (Fully Sharded Data Parallel)
- **Non funziona in Jupyter Notebook** — richiede script standalone lanciati con `torchrun`
- **Overhead di comunicazione**: per dataset/modelli molto piccoli, il multi-GPU può non dare benefici

---

## Fonti

- [[pytorch-in-one-hour]] — Sezione 9 (Sebastian Raschka, 2025)

[^1]: Fonte: [[pytorch-in-one-hour]]

---

*Pagina creata da ingestione di [[pytorch-in-one-hour]]*
