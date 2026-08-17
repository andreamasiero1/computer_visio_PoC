---
title: "Modelli di Ricavo VisAi"
type: concept
created: 2026-07-27
updated: 2026-07-27
tags: [business-model, revenue, saas, pricing, startup, go-to-market]
domain: "Business / Strategy"
complexity: intermediate
confidence: high
related: ["[[retail-shrinkage]]", "[[computer-vision-retail-security]]", "[[product-strategy-lean-vs-full]]", "[[competitor-analysis-loss-prevention]]"]
---

# 🧩 Modelli di Ricavo VisAi

> Analisi dei due modelli di ricavo principali per VisAi: SaaS (canone ricorrente) e Pay-per-Prevention (fee per furto sventato certificato). Include proiezioni finanziarie su OVS e Mango.

---

## Modello A: SaaS (Software-as-a-Service)

### Struttura

Canone mensile ricorrente per negozio. Hardware (server Edge + telecamere) venduto separatamente come CAPEX una tantum.

### Pricing per tier

| Tier | Telecamere | Canone/mese |
|------|-----------|-------------|
| **S** (negozio piccolo) | ≤6 | €290/mese |
| **M** (negozio medio) | 7-10 | €450/mese |
| **L** (negozio grande) | 11-16 | €690/mese |
| **Enterprise** (flagship) | >16 | Custom |

### Setup una tantum

| Voce | Costo |
|------|-------|
| Server Edge (HW + installazione) | €4.500 – €6.000 |
| Telecamere (6-10 × €200-400) | €1.200 – €4.000 |
| Installazione + calibrazione | €1.000 – €1.500 |
| **Totale** | **€6.700 – €11.500** |

### Incluso nel canone

- Software AI completo
- Aggiornamenti modelli AI OTA
- Dashboard + analytics
- Supporto tecnico 7/7
- Monitoraggio remoto salute sistema
- Report mensili Loss Prevention

### Proiezione — OVS (800 negozi target)

| Anno | Negozi | ARR SaaS | Ricavo HW | Totale |
|------|--------|----------|-----------|--------|
| 1 | 50 | €222K | €425K | **€647K** |
| 2 | 200 | €888K | €1.275K | **€2.163K** |
| 3 | 500 | €2.520K | €2.550K | **€5.070K** |
| 4 | 800 | **€4.032K** | €2.550K | **€6.582K** |

### Proiezione — Mango (600 negozi target)

| Anno | Negozi | ARR SaaS | Ricavo HW | Totale |
|------|--------|----------|-----------|--------|
| 1 | 30 | €151K | €315K | **€466K** |
| 2 | 120 | €605K | €945K | **€1.550K** |
| 3 | 300 | €1.620K | €1.890K | **€3.510K** |
| 4 | 600 | **€3.240K** | €3.150K | **€6.390K** |

---

## Modello B: Pay-per-Prevention

### Struttura

Canone base ridotto + bounty fee per ogni furto sventato e **certificato** dal sistema.

### Pricing

| Componente | Prezzo |
|-----------|--------|
| Canone base S (≤6 cam) | €120/mese |
| Canone base M (7-10 cam) | €190/mese |
| Canone base L (11-16 cam) | €290/mese |
| **Fee furto singolo sventato** | **€75/evento** |
| **Fee furto ORC sventato** | **€200/evento** |
| Cap mensile per negozio | €600/mese |

### Certificazione di un furto sventato

Un evento è "certificato" quando:
1. Alert generato dal sistema con anomaly score ≥ threshold
2. Intervento del personale di sicurezza registrato
3. Conferma dell'evento tramite dashboard (1-click)
4. Referto digitale con timestamp + frame anonimizzati
5. Stima valore merce recuperata (integrazione POS/RFID opzionale)

### Stima eventi per negozio

| Parametro | Valore |
|-----------|--------|
| Episodi furto/tentato furto per negozio/anno | 80 – 200 |
| Detection rate VisAi (target) | 85% |
| Tasso di sventamento (alert → intervento) | 50–65% |
| **Furti sventati certificabili/anno** | **34 – 110** |
| **Media mensile** | **3 – 9/mese** |

### Proiezione — OVS (800 negozi, 5 eventi/mese)

| Anno | Negozi | ARR | Ricavo HW | Totale |
|------|--------|-----|-----------|--------|
| 1 | 50 | €339K | €425K | **€764K** |
| 2 | 200 | €1.356K | €1.275K | **€2.631K** |
| 3 | 500 | €3.390K | €2.550K | **€5.940K** |
| 4 | 800 | **€5.424K** | €2.550K | **€7.974K** |

---

## Confronto A vs B

| Metrica | SaaS | Pay-per-Prevention |
|---------|------|--------------------|
| ARR a regime (OVS, 800 neg.) | €4.032K | €5.424K |
| Ricavo/negozio/mese | €420 | €565 |
| Prevedibilità ricavi | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Facilità di vendita | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Allineamento incentivi | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Rischio per VisAi | Basso | Medio |

---

## Raccomandazione

**Modello ibrido: SaaS con bonus performance**

- Canone SaaS base (€290-450/mese) per revenue prevedibile
- Bonus trimestrale legato alla riduzione % delle differenze inventariali
- Go-to-market in 4 fasi: Pilota gratuito → Pay-per-Prevention → SaaS + bonus → Enterprise multi-anno

---

## Benchmark vs. costi LP tradizionale

| Voce | Costo annuo per negozio |
|------|------------------------|
| Sistema EAS (antenne + manutenzione) | €500 – €1.500 |
| Placche/tag | €300 – €800 |
| Manodopera applicazione/rimozione | €2.000 – €5.000 |
| Falsi allarmi (tempo staff, CX) | €500 – €1.500 |
| Guardia giurata | €15.000 – €35.000 |
| **Totale LP tradizionale** | **€18.300 – €43.800** |
| **Costo VisAi SaaS Tier M** | **€5.040 – €5.400** |

---

## Connessione con altri concetti

- [[retail-shrinkage]] — Il problema che genera il mercato
- [[computer-vision-retail-security]] — La soluzione tecnologica
- [[product-strategy-lean-vs-full]] — Impatto della strategia di prodotto sul pricing
- [[competitor-analysis-loss-prevention]] — Benchmark competitivo

---

## Fonti

- Analisi interna VisAi — Luglio 2026
- NRF Security Survey — benchmark shrinkage
- Analisi costi EAS — industry benchmark
- OVS S.p.A. — Bilancio FY 2025
- Mango — Annual Report 2025

---

*Pagina creata da analisi business — 2026-07-27*
