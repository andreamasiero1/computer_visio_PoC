---
title: "Competitor Analysis: Loss Prevention AI"
type: concept
created: 2026-07-27
updated: 2026-07-27
tags: [competitor, veesion, amazon, standard-ai, loss-prevention, market, benchmark]
domain: "Business / Competitive Intelligence"
complexity: intermediate
confidence: high
related: ["[[product-strategy-lean-vs-full]]", "[[revenue-models-visai]]", "[[retail-shrinkage]]", "[[computer-vision-retail-security]]"]
---

# 🧩 Competitor Analysis: Loss Prevention AI

> Analisi dei principali competitor e casi studio nel mercato della loss prevention basata su computer vision. Include Veesion (principale competitor diretto), Amazon JWO, Standard Cognition/AI.

---

## Mappa competitiva

### Quadrante strategico

```
                    COPERTURA TELECAMERE
                    
           Esistenti (plug-in)    Proprietarie (full)
           ─────────────────────────────────────────
    Alto  │                      │                    │
          │  🟢 Veesion          │  🔴 Amazon JWO     │
    FOCUS │  🟡 VisAi (Fase 1)   │  🔴 Standard AI    │
    LP    │  🟢 Vaak             │  🔴 Grabango       │
          │  🟢 Deep North       │                    │
          │──────────────────────│────────────────────│
    FOCUS │                      │                    │
    OPER. │  🟢 RetailNext       │  🔵 Amazon Dash    │
          │  🟢 Sensormatic      │     Cart           │
   Basso  │                      │  🟡 VisAi (Fase 3) │
           ─────────────────────────────────────────
           
    🟢 = attivo e scalato   🔴 = fallito/pivotato   🟡 = VisAi   🔵 = nicchia
```

---

## Competitor Principali

### 1. Veesion (Francia) — Competitor diretto

| Metrica | Dato |
|---------|------|
| **Fondazione** | 2018 |
| **Sede** | Parigi, Francia |
| **Modello** | Behavioral analysis su CCTV esistenti (gesto di occultamento) |
| **Negozi attivi** | **5.000+** in 25+ paesi |
| **ARR** | **~$27,2M** |
| **Funding totale** | **$80M** (incl. Series B $43M, maggio 2025) |
| **Valutazione** | ~$81,5M (pre-Serie B) |
| **Compatibilità CCTV** | ~90% delle telecamere digitali e analogiche |
| **Riduzione furti** | Fino al 60% (80% in un caso UK) |
| **Detection rate** | >90% nelle aree monitorate (vs <5% tradizionale) |
| **Privacy** | NO facial recognition; indagine CNIL su Art. 21 GDPR |

**Punti di forza:**
- Scale provata (5.000 negozi)
- Plug-and-play su CCTV esistenti
- Multi-settore (grocery, fashion, convenience)

**Punti di debolezza:**
- Problemi con CNIL (GDPR Art. 21, diritto di opposizione)
- Non è specializzato nel fashion
- Non fa conteggio capi ai camerini
- Non ha face blurring nativo (rischio EU AI Act)
- Approccio generico, non specifico per abbigliamento

### Differenziazione VisAi vs Veesion

| Differenziatore | Veesion | VisAi |
|----------------|---------|-------|
| Privacy | Indagine CNIL | Face blurring on-the-edge nativo |
| Architettura | Non chiaro se full edge | Edge AI pura: zero dati fuori dal negozio |
| EU AI Act | Rischio "alto rischio" | Design conforme ab initio |
| Settore | Multi-settore generico | **Fashion retail puro** (specializzazione) |
| Roadmap | Solo behavioral | Behavioral → Camerini → Object tracking |
| Conteggio camerini | ❌ | ✅ (Fase 2) |

---

### 2. Amazon Just Walk Out — Caso studio (full tracking)

| Metrica | Dato |
|---------|------|
| **Lancio** | 2018 (Amazon Go) |
| **Tecnologia** | Sensor fusion: cam overhead + sensori peso scaffali + deep learning multimodale |
| **Costo iniziale** | ~$4M/anno per store 1.000 sqft (2017) |
| **Costo dopo ottimizzazione** | ~$159K/anno (2021) — riduzione 96% |
| **Esito grocery** | **Ritirato** da Amazon Fresh USA (2024) |
| **Motivi** | Scalabilità insufficiente, dipendenza revisori umani (India), costi |
| **Dove sopravvive** | 360+ sedi B2B (stadi, aeroporti, ospedali) |
| **Shift** | Da "full-store retrofit" a "lane approach" (zone focalizzate) |

**Lezione**: anche Amazon con risorse illimitate non è riuscita a far funzionare il tracking totale in grandi spazi retail.

---

### 3. Standard Cognition / Standard AI — Caso studio (pivot)

| Metrica | Dato |
|---------|------|
| **Funding** | $200M+ |
| **Obiettivo originale** | Autonomous checkout-free stores |
| **Esito** | **Pivot completo** (marzo 2024): da checkout-free a Vision Analytics |
| **Cambio** | Licenziamenti, nuovo CEO, nuovo CTO |
| **Motivi** | Alti costi infrastrutturali, gap pilota→deploy, dati non pronti |
| **Nuovo focus** | AI per loss prevention e analytics su infrastruttura esistente |

**Lezione**: $200M+ investiti nell'Approccio B → pivot forzato verso Approccio A.

---

## Pricing di mercato — Benchmark

| Segmento | Range pricing | Modello |
|----------|-------------|---------|
| CV SaaS LP (generico) | $50–$500/mese per store | Subscription |
| Veesion (stimato) | ~$450/mese per store | Subscription |
| **VisAi (proposto)** | **€290–€690/mese** | SaaS / ibrido |
| Payback period medio | 14–22 mesi | Industry report |
| Riduzione shrinkage attesa | 25%–40% entro 18 mesi | Industry report |

---

## Connessione con altri concetti

- [[product-strategy-lean-vs-full]] — La decisione strategica informata da questi competitor
- [[revenue-models-visai]] — Pricing posizionato vs. benchmark
- [[retail-shrinkage]] — Il mercato che tutti cercano di servire
- [[action-recognition]] — Tecnologia core condivisa
- [[edge-ai]] — Architettura differenziante

---

## Fonti

- Veesion — [veesion.io](https://veesion.io), [Retail Tech Innovation Hub](https://retailtechinnovationhub.com)
- Veesion funding — [EU-Startups](https://eu-startups.com), [GetLatka](https://getlatka.com), [PitchBook](https://pitchbook.com)
- Veesion CNIL — [Tech-Litigation](https://tech-litigation.com), [CNIL](https://cnil.fr)
- Amazon JWO — [JustWalkOut.com](https://justwalkout.com), [CSP Daily News](https://cspdailynews.com)
- Standard AI — [Standard.ai](https://standard.ai), [CSP Daily News](https://cspdailynews.com)
- Business Insider — Veesion behavioral AI coverage
- CBS News — Veesion case study

---

*Pagina creata da competitive intelligence analysis — 2026-07-27*
