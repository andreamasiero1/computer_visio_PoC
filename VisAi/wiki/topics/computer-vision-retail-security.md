---
title: "Computer Vision per la Sicurezza Retail"
type: topic
created: 2026-07-18
updated: 2026-08-19
tags: [computer-vision, retail, antitaccheggio, sicurezza, startup, edge-ai, cascade-funnel, capo-vivo]
confidence: high
related: ["[[edge-ai]]", "[[action-recognition]]", "[[object-counting]]", "[[pytorch]]", "[[deep-learning-nlp]]", "[[retail-shrinkage]]", "[[revenue-models-visai]]", "[[product-strategy-lean-vs-full]]", "[[competitor-analysis-loss-prevention]]", "[[cascade-funnel-pipeline]]", "[[capo-vivo]]", "[[logica-booleana-allarme]]"]
---

# 🗂️ Computer Vision per la Sicurezza Retail

> Area tematica che copre l'applicazione della computer vision alla prevenzione dei furti nel settore retail, con focus sull'architettura Edge AI e sulla pipeline a imbuto (Cascade Funnel).

---

## Panoramica

Questo topic traccia lo sviluppo del progetto **VisAi**: una soluzione AI-powered per sostituire completamente i sistemi antitaccheggio fisici (placche, antenne acustiche/vettoriali) nei negozi di abbigliamento. L'approccio è basato su computer vision, Edge AI e hardware proprietario con logiche a imbuto per azzerare falsi positivi e saturazione computazionale.

---

## Problema

I sistemi antitaccheggio tradizionali hanno limitazioni significative:

| Problema | Impatto |
|----------|---------|
| **Falsi allarmi** | Costi operativi, esperienza cliente negativa |
| **Costo delle placche** | Fornitura, applicazione, rimozione — labor-intensive |
| **Impatto estetico** | Le placche rovinano l'aspetto dei capi |
| **Efficacia limitata** | Le placche possono essere rimosse o schermate manualmente |

---

## Soluzione VisAi: Flusso Sequenziale a 5 Fasi

VisAi implementa un'architettura **[[cascade-funnel-pipeline]]** a 5 fasi con regole di dominio stringenti:

```
[ Frame Video ] ──► [ Fase 1: Mask Zone Morte + Face Blur ]
                         │
                         ▼
                    [ Fase 2: Person Detection & Spazializzazione ]
                         │
                         ▼
                    [ Fase 3: Rilevamento CAPO VIVO da Zona Morta ]
                         │
                         ▼
                    [ Fase 4: Action Recognition su Intersezione Persona-Capo ]
                         │
                         ▼
                    [ Fase 5: Timer 10s Doppia Verifica ] ──► 🚨 ALLARME
```

### Regole di Dominio e Business
- **GUI Zone Morte**: Mappatura deterministica da interfaccia grafica di scaffali e rack (zero costo AI).
- **Esclusione Cestini**: Focus su retail senza carrelli/borse shopping per eliminare occlusioni lecite.
- **Filtro Dimensione/Valore**: Tracciamento limitato a capi > €40-50 (giacche, maglieria, pantaloni).
- **Esclusione Ingresso**: Nessun allarme per indumenti personali portati dall'esterno.
- **[[logica-booleana-allarme]]**: Allarme scatta solo se esiste Capo Vivo, viene rilevato gesto sospetto e il capo non ricompare entro 10 secondi.

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
| **EU AI Act** | Oscuramento volti on-the-edge (Fase 1) — il sistema non identifica individui |
| **Ispettorato del Lavoro** | Gestione autorizzazioni per monitoraggio in ambiente lavorativo |
| **Sindacati** | Negoziazione e trasparenza sul monitoraggio dei dipendenti |

---

## Concetti chiave

### Architettura & Computer Vision
- [[cascade-funnel-pipeline]] — Architettura a imbuto per Edge AI
- [[capo-vivo]] — Tracciamento selettivo dei prodotti prelevati da zone morte
- [[logica-booleana-allarme]] — Equazione di allarme con doppia verifica temporale 10s
- [[edge-ai]] — Architettura di processing locale on-premise
- [[action-recognition]] — Riconoscimento azioni e stima posa mirata su ROI
- [[object-counting]] — Conteggio e re-identificazione oggetti per camerini

### Business & Strategia
- [[retail-shrinkage]] — Dati sulle differenze inventariali (OVS: €8-10M/anno furti, Mango: €12-15M/anno)
- [[revenue-models-visai]] — SaaS (€290-690/mese) e Pay-per-Prevention (€75/furto)
- [[product-strategy-lean-vs-full]] — Lean vs Full Revolution con casi studio
- [[competitor-analysis-loss-prevention]] — Veesion, Amazon JWO, Standard AI

---

## Domande aperte

- ~~Come calibrare la soglia di alert per avere zero falsi positivi?~~ → **Risolto**: combinazione di [[capo-vivo]] + [[logica-booleana-allarme]] con validazione a timer 10s
- ~~Quale modello di business (SaaS vs performance) sarà più efficace?~~ → **Risolto**: modello ibrido SaaS + bonus performance — vedi [[revenue-models-visai]]
- Quali modelli (YOLO, DETR, SlowFast, ViTPose) funzionano meglio su hardware Edge?
- Come ottimizzare il Face Blurring in testa alla pipeline per latenza sub-millisecondo?
- ~~Telecamere proprietarie o esistenti?~~ → **Risolto**: esistenti per Fase 1, proprietarie per Fase 3 — vedi [[product-strategy-lean-vs-full]]

---

## Fonti correlate

- [[visai-progetto-readme]] — Documento fondativo del progetto
- [[architettura-flusso-sequenziale]] — Flusso sequenziale a 5 fasi e logica di allarme
- NRF, ECR Europe / GRTB — Benchmark shrinkage
- Veesion.io, Amazon JWO, Standard AI — Casi studio competitor
- OVS S.p.A., Mango — Dati finanziari target

---

*Ultimo aggiornamento: 2026-08-19 — Ingestione di [[architettura-flusso-sequenziale]]*
