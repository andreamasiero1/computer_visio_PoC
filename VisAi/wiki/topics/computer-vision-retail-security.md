---
title: "Computer Vision per la Sicurezza Retail"
type: topic
created: 2026-07-18
updated: 2026-07-27
tags: [computer-vision, retail, antitaccheggio, sicurezza, startup, edge-ai]
confidence: high
related: ["[[edge-ai]]", "[[action-recognition]]", "[[object-counting]]", "[[pytorch]]", "[[deep-learning-nlp]]", "[[retail-shrinkage]]", "[[revenue-models-visai]]", "[[product-strategy-lean-vs-full]]", "[[competitor-analysis-loss-prevention]]"]
---

# 🗂️ Computer Vision per la Sicurezza Retail

> Area tematica che copre l'applicazione della computer vision alla prevenzione dei furti nel settore retail, con focus sull'architettura Edge AI.

---

## Panoramica

Questo topic traccia lo sviluppo del progetto **VisAi**: una soluzione AI-powered per sostituire completamente i sistemi antitaccheggio fisici (placche, antenne acustiche/vettoriali) nei negozi di abbigliamento. L'approccio è basato su computer vision, Edge AI e hardware proprietario.

---

## Problema

I sistemi antitaccheggio tradizionali hanno limitazioni significative:

| Problema | Impatto |
|----------|---------|
| **Falsi allarmi** | Costi operativi, esperienza cliente negativa |
| **Costo delle placche** | Fornitura, applicazione, rimozione — labor-intensive |
| **Impatto estetico** | Le placche rovinano l'aspetto dei capi |
| **Efficacia limitata** | Le placche possono essere rimosse o schermatemanualmente |

---

## Soluzione VisAi

### Architettura

```
[Telecamere proprietarie] → [Server Edge locale] → [Alert in tempo reale]
         ↓                          ↓
    Video stream            Processing on-premise
                            (zero cloud, zero latenza)
```

### Due feature core

1. **[[action-recognition]]** — Anomaly detection comportamentale per rilevare occultamento merce
2. **[[object-counting]]** — Conteggio capi entrata/uscita camerini via Re-Identification

### Stack tecnologico

- **[[edge-ai]]** — Architettura pura edge, server locale per negozio
- **[[pytorch]]** — Framework per training e implementazione dei modelli
- **Hardware proprietario** — Telecamere ottimizzate per il software

---

## Aspetti business

| Aspetto | Stato |
|---------|-------|
| **Target** | ✅ Validato: Grandi catene Retail (OVS, Mango, fast fashion) — vedi [[retail-shrinkage]] |
| **Business model** | ✅ Definito: SaaS ibrido con bonus performance — vedi [[revenue-models-visai]] |
| **Go-to-market** | ✅ Definito: 4 fasi (pilota gratuito → pay-per-prevention → SaaS → enterprise) |
| **Value proposition** | Eliminazione placche → risparmio tempo staff, estetica capi, ROI |
| **Competitor principale** | Veesion (5.000 negozi, $27M ARR) — vedi [[competitor-analysis-loss-prevention]] |
| **Strategia di prodotto** | ✅ Deciso: Lean (cam esistenti) ora → Full Revolution come evoluzione — vedi [[product-strategy-lean-vs-full]] |
| **Proiezione ARR (a regime)** | €4-5M per singolo contratto enterprise (OVS/Mango) |

---

## Compliance legale

| Normativa | Strategia |
|-----------|-----------|
| **GDPR** | Dati processati localmente, non trasferiti a terzi |
| **EU AI Act** | Oscuramento volti on-the-edge — il sistema non identifica individui |
| **Ispettorato del Lavoro** | Gestione autorizzazioni per monitoraggio in ambiente lavorativo |
| **Sindacati** | Negoziazione e trasparenza sul monitoraggio dei dipendenti |

---

## Concetti chiave

### Tecnici
- [[edge-ai]] — Architettura di processing locale
- [[action-recognition]] — Riconoscimento azioni e stima posa
- [[object-counting]] — Conteggio e re-identificazione oggetti

### Business & Strategia
- [[retail-shrinkage]] — Dati sulle differenze inventariali (OVS: €8-10M/anno furti, Mango: €12-15M/anno)
- [[revenue-models-visai]] — SaaS (€290-690/mese) e Pay-per-Prevention (€75/furto)
- [[product-strategy-lean-vs-full]] — Lean vs Full Revolution con casi studio
- [[competitor-analysis-loss-prevention]] — Veesion, Amazon JWO, Standard AI

---

## Domande aperte

- ~~Quale modello di business (SaaS vs performance) sarà più efficace?~~ → **Risolto**: modello ibrido SaaS + bonus performance — vedi [[revenue-models-visai]]
- Come calibrare la soglia di alert per avere zero falsi positivi?
- Quali modelli (YOLO, DETR, SlowFast, ViTPose) funzionano meglio su hardware Edge?
- Come gestire scenari di negozio affollato (occlusioni, tracking multi-persona)?
- Quale sarà la compliance richiesta per il mercato USA vs EU?
- ~~Telecamere proprietarie o esistenti?~~ → **Risolto**: esistenti per Fase 1, proprietarie per Fase 3 — vedi [[product-strategy-lean-vs-full]]

---

## Fonti correlate

- [[visai-progetto-readme]] — Documento fondativo del progetto
- NRF, ECR Europe / GRTB — Benchmark shrinkage
- Veesion.io, Amazon JWO, Standard AI — Casi studio competitor
- OVS S.p.A., Mango — Dati finanziari target

---

*Pagina aggiornata con analisi business e strategia — 2026-07-27*
