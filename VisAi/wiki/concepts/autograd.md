---
title: "Autograd (Automatic Differentiation)"
type: concept
created: 2026-07-18
updated: 2026-07-18
tags: [autograd, backpropagation, gradienti, differenziazione-automatica, pytorch, deep-learning]
domain: "Deep Learning / Ottimizzazione"
complexity: intermediate
confidence: high
related: ["[[pytorch]]", "[[tensor]]", "[[transformer]]", "[[deep-learning-nlp]]"]
---

# 🧩 Autograd (Differenziazione Automatica)

> Il motore di PyTorch che calcola automaticamente i gradienti costruendo e percorrendo grafi computazionali. Rende il backpropagation trasparente per l'utente.

---

## Definizione

**Autograd** (automatic differentiation/gradient) è il sistema di PyTorch che traccia ogni operazione eseguita sui tensori, costruisce un **grafo computazionale** diretto (DAG), e lo percorre al contrario per calcolare i gradienti della loss function rispetto ai parametri del modello. Questo processo è chiamato **reverse-mode automatic differentiation** o, nel contesto delle reti neurali, **backpropagation**.

---

## Come funziona

### 1. Costruzione del grafo

Quando un tensore ha `requires_grad=True`, PyTorch traccia ogni operazione creando un grafo computazionale in background:

```python
w1 = torch.tensor([2.2], requires_grad=True)
b = torch.tensor([0.0], requires_grad=True)
x1 = torch.tensor([1.1])

z = x1 * w1 + b           # PyTorch traccia questa operazione
a = torch.sigmoid(z)       # ...e questa
loss = F.binary_cross_entropy(a, y)  # ...e questa
```

### 2. Calcolo dei gradienti

```python
loss.backward()  # Percorre il grafo al contrario (backpropagation)

print(w1.grad)   # Gradiente di loss rispetto a w1
print(b.grad)    # Gradiente di loss rispetto a b
```

### 3. La chain rule

Il backpropagation è un'implementazione della **regola della catena** (chain rule) dal calcolo differenziale. Partendo dalla loss, si calcolano le derivate parziali a ritroso attraverso il grafo, concatenandole:

```
∂Loss/∂w1 = ∂Loss/∂a · ∂a/∂z · ∂z/∂w1
```

PyTorch fa tutto questo automaticamente — **non serve calcolare derivate a mano** [^1].

---

## Concetti chiave

| Concetto | Spiegazione |
|----------|-------------|
| `requires_grad=True` | Dice a PyTorch di tracciare le operazioni su questo tensore |
| `grad_fn` | Funzione che ha generato un tensore nel grafo (es. `<AddmmBackward0>`) |
| `loss.backward()` | Calcola tutti i gradienti dei leaf nodes del grafo |
| `.grad` | Attributo del tensore che contiene il gradiente calcolato |
| `torch.no_grad()` | Context manager che disattiva il tracking (per inferenza) |
| `optimizer.zero_grad()` | **Fondamentale**: azzerare i gradienti prima di ogni iterazione, altrimenti si accumulano |

---

## Il Training Loop standard

```python
for epoch in range(num_epochs):
    model.train()
    for features, labels in train_loader:
        logits = model(features)                    # Forward pass
        loss = F.cross_entropy(logits, labels)      # Calcolo loss
        optimizer.zero_grad()                       # Azzerare gradienti
        loss.backward()                             # Backpropagation
        optimizer.step()                            # Aggiornamento pesi
    model.eval()
```

### Perché `zero_grad()` non è automatico?

PyTorch non azzera i gradienti automaticamente perché in alcuni casi è utile **accumularli** (gradient accumulation), ad esempio per simulare batch size più grandi su GPU con memoria limitata [^2].

---

## Modalità del modello

| Modalità | Metodo | Quando usarla |
|----------|--------|--------------|
| Training | `model.train()` | Durante il training (attiva dropout, batch norm) |
| Evaluation | `model.eval()` | Durante inferenza/test |
| No gradient | `torch.no_grad()` | Per inferenza — risparmia memoria e calcolo |

---

## Fonti

- [[pytorch-in-one-hour]] — Sezioni 3, 4, 7 (Sebastian Raschka, 2025)

[^1]: Fonte: [[pytorch-in-one-hour]] — "all you need to take away from this section is that PyTorch takes care of the calculus for us via the `.backward` method"
[^2]: Fonte: [[pytorch-in-one-hour]] — "In some instances, it may be desirable to accumulate the gradients"

---

*Pagina creata da ingestione di [[pytorch-in-one-hour]]*
