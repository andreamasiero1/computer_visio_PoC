---
title: "PyTorch in One Hour: From Tensors to Training Neural Networks on Multiple GPUs"
type: source
source_type: article
created: 2026-07-18
updated: 2026-07-18
tags: [pytorch, deep-learning, tensori, autograd, gpu, ddp, tutorial]
sources: ["raw/PyTorch in One Hour From Tensors to Training Neural Networks on Multiple GPUs.md"]
author: "Sebastian Raschka"
date_published: 2025-07-02
url: "https://sebastianraschka.com/teaching/pytorch-1h/"
confidence: high
related: ["[[transformer]]", "[[self-attention]]", "[[tensor]]", "[[autograd]]", "[[distributed-data-parallel]]", "[[pytorch]]", "[[sebastian-raschka]]", "[[deep-learning-nlp]]"]
---

# 📄 PyTorch in One Hour

> Tutorial curato da Sebastian Raschka che copre i fondamentali di PyTorch in circa un'ora di lettura: dai tensori al training di reti neurali su GPU multiple.

---

## Riassunto

Questo articolo è un **tutorial pratico e strutturato** su PyTorch, scritto da Sebastian Raschka, ricercatore e autore di riferimento nel campo del deep learning. Copre i concetti essenziali necessari per iniziare a implementare reti neurali profonde, inclusi i Large Language Models (LLMs).

L'articolo è organizzato in 9 sezioni principali che seguono un percorso progressivo:

1. **Cos'è PyTorch**: libreria open-source Python per il deep learning, la più usata nella ricerca dal 2019. Ha 3 componenti core: una libreria di tensori (con supporto GPU), un motore di differenziazione automatica (autograd), e utilità per il deep learning.

2. **Tensori**: strutture dati fondamentali che generalizzano scalari, vettori e matrici. PyTorch usa `float32` di default per bilanciare precisione ed efficienza computazionale su GPU. L'API è molto simile a NumPy.

3. **Grafi computazionali**: PyTorch costruisce automaticamente in background un grafo diretto delle operazioni, necessario per il backpropagation. Ogni operazione matematica diventa un nodo del grafo.

4. **Differenziazione automatica (Autograd)**: il motore autograd di PyTorch traccia ogni operazione sui tensori e, chiamando `loss.backward()`, calcola automaticamente tutti i gradienti necessari per l'aggiornamento dei pesi. Non serve calcolo differenziale manuale.

5. **Implementazione di reti neurali**: si sottoclassa `torch.nn.Module`, definendo i layer nel costruttore `__init__` e il forward pass nel metodo `forward`. Esempio concreto con multilayer perceptron.

6. **Data Loaders**: `Dataset` e `DataLoader` di PyTorch gestiscono il caricamento efficiente dei dati. `Dataset` definisce come accedere ai singoli campioni, `DataLoader` gestisce shuffling e batching. `num_workers > 0` permette il caricamento parallelo.

7. **Training loop**: il pattern standard è: forward pass → calcolo loss → `optimizer.zero_grad()` → `loss.backward()` → `optimizer.step()`. Usare `model.train()` e `model.eval()` per gestire i diversi comportamenti.

8. **Salvataggio e caricamento modelli**: usare `torch.save(model.state_dict(), "model.pth")` per salvare e `model.load_state_dict(torch.load(...))` per caricare.

9. **Training su GPU**: passare da CPU a GPU richiede solo `.to("cuda")`. Per il multi-GPU, `DistributedDataParallel` (DDP) divide i dati tra GPU, sincronizza i gradienti e scala quasi linearmente. Si lancia con `torchrun`.

---

## Key Takeaways

- **PyTorch = 3 componenti**: tensor library + autograd engine + deep learning utilities
- **Tensori come fondamento**: generalizzano array multidimensionali, con default `float32` per efficienza GPU
- **Autograd elimina il calcolo manuale**: `loss.backward()` fa tutto il lavoro di calcolo dei gradienti
- **Training loop standardizzato**: forward → loss → zero_grad → backward → step
- **GPU computing è semplice**: basta `.to("cuda")` per spostare tensori e modelli
- **DDP per multi-GPU**: scala quasi linearmente, si lancia con `torchrun --nproc_per_node=N`
- **Best practice**: usare `torch.no_grad()` per inferenza, `model.train()`/`model.eval()` per cambiare modalità, `drop_last=True` per batch uniformi

---

## Citazioni rilevanti

> "PyTorch has been the most widely used deep learning library for research since 2019 by a wide margin." [^1]

> "One of the reasons why PyTorch is so popular is its user-friendly interface and efficiency. However, despite its accessibility, it doesn't compromise on flexibility." [^1]

> "While this calculus jargon was a means to explain PyTorch's autograd component, all you need to take away from this section is that PyTorch takes care of the calculus for us via the `.backward` method." [^1]

> "Barring a minor communication overhead between devices that comes with DDP use, it can theoretically process a training epoch in half the time with two GPUs compared to just one." [^1]

[^1]: Fonte: [PyTorch in One Hour](../raw/PyTorch%20in%20One%20Hour%20From%20Tensors%20to%20Training%20Neural%20Networks%20on%20Multiple%20GPUs.md) — Sebastian Raschka, 2025

---

## Pagine wiki collegate

- **Entità**: [[sebastian-raschka]], [[pytorch]]
- **Concetti**: [[tensor]], [[autograd]], [[distributed-data-parallel]], [[transformer]]
- **Topic**: [[deep-learning-nlp]]

---

*Pagina creata da ingestione #2 — 2026-07-18*
