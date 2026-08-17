---
title: "Product Strategy: Lean vs Full Revolution"
type: concept
created: 2026-07-27
updated: 2026-07-27
tags: [strategy, product, startup, go-to-market, decision, architecture]
domain: "Business / Product Strategy"
complexity: advanced
confidence: high
related: ["[[computer-vision-retail-security]]", "[[revenue-models-visai]]", "[[retail-shrinkage]]", "[[competitor-analysis-loss-prevention]]", "[[action-recognition]]", "[[object-counting]]", "[[edge-ai]]"]
---

# 🧩 Product Strategy: Lean vs Full Revolution

> Analisi strategica della decisione fondamentale di VisAi: utilizzare telecamere già installate nei negozi (Lean) o implementare copertura 360° proprietaria con object tracking per singolo capo (Full Revolution). Decisione presa: **Lean ora → Full come evoluzione.**

---

## Le due visioni

| | 🅰️ Approccio Lean | 🅱️ Approccio Full Revolution |
|--|-------------------|------------------------------|
| **Cosa fa** | Analisi comportamentale AI su telecamere già installate | Object tracking per singolo capo + behavioral su copertura 360° proprietaria |
| **Telecamere** | Esistenti del retailer (4-15 per negozio) | Proprietarie VisAi (25-50 per negozio) |
| **Detection** | Riconosce gesti sospetti (occultamento) | Traccia OGNI capo + riconosce gesti → certifica il furto |
| **Installazione** | Mini-server Edge + plug-in su CCTV esistente | Rifacimento completo impianto video + server enterprise |
| **Ambizione** | Migliorare la loss prevention esistente | Sostituire completamente l'antitaccheggio tradizionale |

---

## Evidenze dai casi studio reali

### ✅ Chi ha fatto l'Approccio A ha scalato

| Azienda | Approccio | Risultato | Fonte |
|---------|-----------|-----------|-------|
| **Veesion** (FR) | Behavioral analysis su CCTV esistenti | 5.000+ negozi, $27M ARR, Series B $43M (2025) | veesion.io, Retail Tech Innovation Hub, GetLatka |
| **Vaak** (JP) | Behavioral analysis su CCTV esistenti | Deployato in convenience stores giapponesi | Press coverage |
| **Deep North** (US) | Analytics + LP su cam esistenti | Scalato in multi-settore | Press coverage |

### ❌ Chi ha provato l'Approccio B come primo prodotto ha fallito

| Azienda | Approccio | Risultato | Fonte |
|---------|-----------|-----------|-------|
| **Amazon JWO** | Full object tracking (cam + sensori peso) | Costo iniziale $4M/store, ridotto 96% a $159K; **ritirato** dai grocery USA (2024), sopravvive solo in 360+ sedi B2B piccole | Amazon reports, CSP Daily News, Retail Dive |
| **Standard Cognition** | Checkout-free con full camera coverage | $200M+ funding → **pivot forzato** a Vision Analytics (2024); licenziamenti, nuovo CEO | CSP Daily News, Standard.ai |
| **Grabango** | Checkout-free | **Chiusura** | Press coverage |

---

## Confronto tecnico

### Telecamere necessarie

| Scenario | N° telecamere | Fonte |
|----------|---------------|-------|
| Fashion store medio — CCTV esistente | 4–15 | CCTVSecurityPros, EmirTech |
| VisAi Approach A | 4–15 (0 nuove) | — |
| VisAi Approach B | 25–50 (quasi tutte nuove) | Stima interna |
| Amazon JWO | Centinaia per 1.000 sqft | Amazon documentation |

### Object tracking di capi d'abbigliamento — Sfide

| Sfida | Gravità | Dettaglio |
|-------|---------|-----------|
| Deformabilità | 🔴 Critica | Un capo non ha forma fissa (vs scatola di cereali) |
| Somiglianza inter-classe | 🔴 Critica | 50 t-shirt nere sullo stesso scaffale |
| Occlusione | 🔴 Critica | Capo nascosto dietro altri, in borse, sotto vestiti |
| Re-ID cross-camera | 🟠 Alta | Stesso capo da angolazioni e luci diverse |
| Cambio di stato | 🟠 Alta | Piegato → aperto → indossato → ripiegato → in borsa |
| Computazione | 🟠 Alta | Tracking simultaneo centinaia di capi → GPU enterprise |
| Dataset | 🟡 Media | Non esistono dataset pubblici per garment tracking retail |

> **Stato dell'arte MOT/Re-ID (2025)**: i paper accademici convergono su approcci "cloth-agnostic" e "occlusion-aware" (Vision Transformers, skeleton dynamics). Tuttavia, INRIA evidenzia che i moduli Re-ID forniscono miglioramenti marginali nei benchmark MOT reali e possono degradare le performance.

### Gestione "dead zones"

L'Approccio B richiede la definizione di zone dove il capo può essere legittimamente posato (appendini, scaffali, display). Problematiche:
- Layout diverso per ogni negozio → configurazione manuale
- Layout cambiano stagionalmente → riconfigurazione
- Display promozionali temporanei → dead zones al volo
- Clienti che posano capi "fuori zona" → falsi positivi
- Staff che sposta capi (riassortimento) → distinguere staff da clienti

---

## Confronto economico

### Costo per negozio

| Voce | Approach A | Approach B |
|------|-----------|-----------|
| Telecamere | €0 | €7.500 – €20.000 |
| Server Edge | €2.500 – €4.000 | €6.000 – €10.000 |
| Installazione | €500 – €1.000 | €3.000 – €6.000 |
| Calibrazione | €300 – €500 | €2.000 – €4.000 |
| **Totale setup** | **€3.300 – €5.500** | **€18.500 – €40.000** |
| **Rapporto** | **1x** | **5-8x** |

### Sviluppo e time-to-market

| Parametro | Approach A | Approach B |
|-----------|-----------|-----------|
| Modelli AI necessari | Person Detection + Pose + Action Classification | Tutto A + Object Detection capi + MOT + Re-ID cross-cam + Dead Zone Mgmt |
| Team AI | 2-3 ML engineers | 5-8 ML engineers + CV researchers |
| Time-to-market (PoC → pilota) | **6-9 mesi** | **18-24 mesi** |
| Costo sviluppo (al pilota) | **€150K – €300K** | **€800K – €1.5M** |
| Rischio tecnico | Medio | Altissimo |

---

## Decisione: Approccio A → B in 3 fasi

### Crossing the Chasm (Geoffrey Moore, 1991)

- **Approccio B** = prodotto da Early Majority (richiede ecosistema maturo, fiducia consolidata)
- **Approccio A** = prodotto giusto per Early Adopters (leggero, integrabile, dimostrabile)
- Lanciare B ora = entrare nella fase Innovators con un prodotto per il mainstream = errore Standard Cognition

### Roadmap in 3 fasi

| Fase | Periodo | Cosa | Perché | KPI |
|------|---------|------|--------|-----|
| **1** | Mesi 0-12 | Behavioral analysis su CCTV esistenti | Time-to-market, revenue, validazione | 50+ negozi, detection >85% |
| **2** | Mesi 12-24 | + 1-2 telecamere camerini → conteggio capi IN/OUT | Differenziazione, upsell, training data | Conteggio >95%, upsell >40% |
| **3** | Mesi 24-36 | Full object tracking nei migliori clienti, copertura 360° | Con dati + revenue di Fase 1-2 | Certificazione furto, sostituzione EAS |

### Perché l'Approccio A non è un compromesso

- Veesion fa $27M ARR con questo approccio → mercato validato
- VisAi si differenzia con: (1) face blurring nativo, (2) edge-only, (3) conteggio camerini in Fase 2
- Ogni negozio in Fase 1 genera dati di training gratuiti per Fase 3
- Con 200 negozi hai le relazioni per proporre l'upgrade
- Con €1-2M ARR puoi fare un round Series A per finanziare la R&D di Fase 3

---

## Connessione con altri concetti

- [[action-recognition]] — Core technology per Approach A
- [[object-counting]] — Aggiunta in Fase 2
- [[edge-ai]] — Architettura per entrambi gli approcci
- [[retail-shrinkage]] — Il problema di mercato
- [[revenue-models-visai]] — Come monetizzare
- [[competitor-analysis-loss-prevention]] — Benchmark competitivo

---

## Fonti

- Amazon JWO — Reports e analisi di settore, CSP Daily News, Retail Dive
- Veesion — veesion.io, Retail Tech Innovation Hub, GetLatka, PitchBook
- Standard Cognition — CSP Daily News, Standard.ai, The Shelby Report
- INRIA — Limitazioni Re-ID in MOT reale
- arXiv / CVPR / ICCV — State-of-the-art object tracking 2024-2025
- Geoffrey Moore — *Crossing the Chasm* (1991)
- Gartner — Hype Cycle, Technology Adoption Lifecycle

---

*Pagina creata da analisi strategica co-founder — 2026-07-27*
