---
title: "Retail Shrinkage (Differenze Inventariali)"
type: concept
created: 2026-07-27
updated: 2026-07-27
tags: [retail, shrinkage, furti, loss-prevention, business, market-analysis]
domain: "Business / Retail"
complexity: basic
confidence: high
related: ["[[computer-vision-retail-security]]", "[[revenue-models-visai]]", "[[product-strategy-lean-vs-full]]"]
---

# 🧩 Retail Shrinkage (Differenze Inventariali)

> Perdite di inventario nel retail dovute a furti esterni, furti interni, errori amministrativi e frodi fornitori. Rappresenta il problema centrale che VisAi si propone di risolvere.

---

## Definizione

Lo **shrinkage** (o **differenze inventariali**) è la differenza tra l'inventario contabile teorico e quello fisico reale di un retailer. Include tutte le perdite di merce non attribuibili a vendite regolari.

### Composizione tipica dello shrinkage

| Causa | % sul totale | Descrizione |
|-------|-------------|-------------|
| **Furti esterni (shoplifting + ORC)** | **~36%** | Taccheggio occasionale + crimine organizzato retail |
| **Furti interni (dipendenti)** | ~29% | Sottrazione merce da parte del personale |
| **Errori amministrativi** | ~21% | Errori di registrazione, conteggio, pricing |
| **Frodi fornitori** | ~14% | Consegne incomplete, fatturazioni errate |

> Fonte: NRF (National Retail Federation) — National Retail Security Survey

---

## Benchmark di settore

### Tasso di shrinkage

| Segmento | Tasso medio (% su ricavi) | Fonte |
|----------|--------------------------|-------|
| Retail generale (Europa) | 1,0% – 1,6% | NRF / GRTB |
| **Fashion apparel** | **1,3% – 2,0%** (fascia alta) | Industry benchmark, ECR Europe |
| Grocery | 0,8% – 1,5% | NRF |
| Elettronica | 1,0% – 1,8% | NRF |

Il fashion apparel è tra le categorie **a più alto rischio** per via dell'alto rapporto valore/dimensione dei capi.

### Trend recenti

| Dato | Valore | Anno | Fonte |
|------|--------|------|-------|
| Shrinkage rate medio retail | ~1,6% dei ricavi | 2022 (ultimo dato NRF ufficiale) | NRF Security Survey |
| Aumento episodi taccheggio | **+19%** YoY | 2023→2024 | NRF / ASIS |
| Perdite shoplifting USA | ~$45 miliardi | 2024 | NRF estimates |
| NRF ha smesso di pubblicare il report shrink tradizionale | — | 2024 | Retail Dive |

> **Nota**: dal 2024 la NRF non pubblica più il report aggregato sullo shrink, sostituendolo con report su retail theft & violence. I dati di settore si basano quindi sull'ultimo survey ufficiale (FY 2022) e su stime derivate.

---

## Applicazione ai target VisAi

### OVS S.p.A.

| Metrica | Valore (FY 2025) |
|---------|-------------------|
| Ricavi netti | €1.746M |
| Negozi | ~2.600 |
| Shrinkage stimato (1,3%–1,6%) | €22,7M – €27,9M/anno |
| Di cui furti esterni (~36%) | **€8,2M – €10,0M/anno** |
| Perdita per furto esterno/negozio | **€3.150 – €3.860/anno** |

### Mango

| Metrica | Valore (FY 2025) |
|---------|-------------------|
| Ricavi totali | €3.800M |
| Ricavi retail fisico (~67%) | €2.546M |
| Negozi | ~2.931 |
| Shrinkage stimato (1,3%–1,6%) | €33,1M – €40,7M/anno |
| Di cui furti esterni (~36%) | **€11,9M – €14,7M/anno** |
| Perdita per furto esterno/negozio | **€4.060 – €5.010/anno** |

> **Nota metodologica**: OVS e Mango non pubblicano dati espliciti sulle differenze inventariali nei bilanci pubblici. OVS accantona un "fondo differenze inventariali" nelle note illustrative al bilancio consolidato. Le stime si basano su benchmark di settore.

---

## Impatto sul margine operativo

Un retailer fashion con margine EBITDA del 12,5% (come OVS) che perde l'1,5% in shrinkage sta cedendo circa il **12% del proprio profitto operativo**. Ogni punto percentuale di riduzione dello shrinkage ha un impatto diretto e significativo sulla bottom line.

---

## Connessione con altri concetti

- [[computer-vision-retail-security]] — La soluzione tecnologica al problema
- [[revenue-models-visai]] — Come VisAi monetizza la riduzione dello shrinkage
- [[product-strategy-lean-vs-full]] — Quale approccio di prodotto per affrontare il problema
- [[action-recognition]] — Tecnologia core per rilevare i furti

---

## Fonti

- NRF (National Retail Federation) — [nrf.com](https://nrf.com)
- ECR Europe / GRTB (Global Retail Theft Barometer)
- OVS S.p.A. — Bilancio consolidato FY 2025 — [ovscorporate.it](https://ovscorporate.it)
- Mango — Annual Report 2025 — [mango.com](https://mango.com)
- Retail Dive — Evoluzione reporting NRF — [retaildive.com](https://retaildive.com)
- ASIS International — Trend shoplifting 2024 — [asisonline.org](https://asisonline.org)

---

*Pagina creata da analisi di mercato — 2026-07-27*
