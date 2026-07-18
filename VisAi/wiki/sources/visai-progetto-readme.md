---
title: "README Progetto VisAi — Anti-Theft AI per Retail"
type: source
source_type: note
created: 2026-07-18
updated: 2026-07-18
tags: [progetto, startup, computer-vision, retail, antitaccheggio, edge-ai, business]
sources: ["README.md"]
author: "Andrea Masiero"
confidence: high
related: ["[[edge-ai]]", "[[action-recognition]]", "[[object-counting]]", "[[computer-vision-retail-security]]", "[[pytorch]]"]
---

# 📄 README Progetto VisAi — Anti-Theft AI per Retail

> Documento fondativo del progetto: una startup che vuole sostituire i sistemi antitaccheggio fisici con computer vision e Edge AI.

---

## Riassunto

Il README descrive la **visione strategica e tecnica** della startup VisAi. L'obiettivo è sviluppare un prodotto basato sull'IA per riconoscere i furti all'interno di negozi di abbigliamento, sostituendo completamente i vecchi sistemi antitaccheggio (placche fisiche e antenne acustiche/vettoriali).

### Pillar della startup

| # | Area | Dettaglio |
|---|------|-----------|
| 1 | **Target** | Grandi catene di Retail (Fast Fashion, grandi magazzini) |
| 2 | **Business Model** | Da validare: SaaS B2B classico vs modello a performance (% sul valore dei furti sventati). Test in "negozi pilota" |
| 3 | **Architettura** | Edge AI pura — server fisico proprietario in ogni punto vendita. Processing locale, latenza zero, massima sicurezza del dato |
| 4 | **Hardware** | Telecamere specifiche e proprietarie, ottimizzate per il software |
| 5 | **Core Feature IA** | (1) Anomaly detection comportamentale + (2) Conteggio capi nei camerini |

### Due core feature dell'IA

1. **Action Recognition / Anomaly Detection**: rilevamento di atteggiamenti sospetti finalizzati all'occultamento intenzionale del capo. Obiettivo: zero falsi positivi (distinguere tra furto e gesti normali come mettere le mani in tasca).

2. **Conteggio capi camerini**: telecamera dedicata agli ingressi/uscite dei camerini con Re-Identification/Object Counting per verificare che il numero di capi in entrata corrisponda a quelli in uscita. Senza violare la privacy dell'interno del camerino.

---

## Key Takeaways

- **Disruption totale**: non un miglioramento dei sistemi esistenti, ma una sostituzione completa delle placche fisiche
- **Edge-first**: scelta architetturale forte — tutto il processing avviene on-premise, nessun cloud. Questo risolve problemi di latenza, privacy e compliance
- **Hardware proprietario**: telecamere custom ottimizzate per il software, non CCTV generiche
- **Business model da validare**: la fase di negozi pilota servirà a definire metriche e KPI per scegliere tra SaaS e performance-based
- **Compliance legale è un differenziatore**: GDPR, EU AI Act (oscuramento volti on-the-edge), gestione delle autorizzazioni con Ispettorato del Lavoro/Sindacati

---

## Roadmap richiesta (da sviluppare)

Il documento richiede una roadmap su due assi:

### 1. Sviluppo Business
- Strategia negozi pilota con metriche per comparare SaaS vs performance
- Analisi competitiva e Value Proposition (risparmio tempo staff, estetica capi, ROI)
- Compliance legale pre-confezionata per i clienti

### 2. Sviluppo Tecnico AI
- Pipeline video Edge AI (ottimizzazione modelli per server locale)
- Action Recognition / Pose Estimation per rilevare l'occultamento
- Algoritmo conteggio capi per zona camerini
- Testing hardware (calibrazione telecamere, stress-test server in negozio affollato)

---

## Citazioni rilevanti

> "Vogliamo sostituire e innovare completamente i vecchi sistemi antitaccheggio (placche fisiche e antenne acustiche/vettoriali) eliminando i falsi allarmi e i costi di fornitura delle placche." [^1]

> "Soluzione Edge AI pura. Installeremo un server fisico proprietario all'interno di ogni punto vendita per processare i video localmente, garantendo latenza zero e massima sicurezza del dato." [^1]

> "Rilevamento di anomalie comportamentali e atteggiamenti sospetti finalizzati all'occultamento intenzionale del capo." [^1]

[^1]: Fonte: [README.md](../../README.md) — Andrea Masiero

---

## Pagine wiki collegate

- **Concetti**: [[edge-ai]], [[action-recognition]], [[object-counting]]
- **Topic**: [[computer-vision-retail-security]]
- **Strumenti**: [[pytorch]] (framework per l'implementazione dei modelli)

---

*Pagina creata da ingestione #3 — 2026-07-18*
