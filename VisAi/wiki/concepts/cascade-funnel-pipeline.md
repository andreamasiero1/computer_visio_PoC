---
title: "Cascade Funnel Pipeline (Architettura a Imbuto)"
type: concept
created: 2026-08-19
updated: 2026-08-19
tags: [cascade-funnel, pipeline, edge-ai, computer-vision, architettura, retail-security]
domain: "Computer Vision / Edge AI"
complexity: intermediate
confidence: high
related: ["[[capo-vivo]]", "[[logica-booleana-allarme]]", "[[edge-ai]]", "[[action-recognition]]", "[[computer-vision-retail-security]]"]
---

# 🌪️ Cascade Funnel Pipeline (Architettura a Imbuto)

> Paradigma architetturale a filtri sequenziali progressivi per ottimizzare le risorse computazionali su Edge AI e ridurre a zero i falsi positivi nei sistemi anti-taccheggio VisAi.

---

## Definizione e Motivazione

Nei negozi retail con centinaia di capi esposti e decine di clienti in movimento simultaneo, l'esecuzione continua di modelli di Visione Artificiale complessi (Action Recognition, Pose Estimation 3D, Spatial-Temporal Transformers) su ogni persona o oggetto causerebbe:
1. **Saturazione immediata delle risorse hardware** (l'Edge server on-premise collasserebbe).
2. **Elevato tasso di falsi allarmi** dovuti a rumore di fondo, occlusione da piccoli accessori o indumenti personali.

Il **Cascade Funnel** risolve questo problema strutturando l'elaborazione come un imbuto a stadi successivi, dove ogni stadio filtra la maggior parte dei dati tramite regole deterministiche o modelli leggeri prima di invocare i moduli ad alta intensità computazionale.

```
[ Frame Video Completo ]
       │
       ▼ (Fase 1: Face Blur + Maschera Zone Morte GUI)
[ Solo Pixel Attivi Fuori Rack ]
       │
       ▼ (Fase 2: Person Detection & Spazializzazione)
[ Coordinate Persone in Corsie Rilevanti ]
       │
       ▼ (Fase 3: Filtro Dimensione + Origine da Zona Morta)
[ Solo Pochi Capi Vivi Tracciati ]
       │
       ▼ (Fase 4: Pose Estimation & Action Recognition su Intersezione)
[ Gesto Sospetto Rilevato ]
       │
       ▼ (Fase 5: Timer 10s Doppia Verifica)
[ ALLARME CONFERMATO ]
```

---

## Fasi dell'Architettura a Imbuto

### 1. Preprocessing e Mascheramento Spaziale
- **Zone Morte Statiche**: Delimitate tramite GUI dall'operatore durante il setup (rack, scaffali, manichini). I pixel all'interno di queste aree vengono ignorati dall'analisi di movimento.
- **Privacy by Design**: Face Blurring applicato direttamente sul frame raw, prima di qualunque operazione di tracking o feature extraction, per conformità al GDPR e all'EU AI Act.

### 2. Person Detection e Contesto Spaziale
- Rilevamento bounding box persone con modelli ultraleggeri (es. YOLO pre-trained).
- Mappatura della posizione per stabilire se il cliente si trova in aree ad alto rischio o corsie generiche.

### 3. Filtro di Dominio e Istanziazione [[capo-vivo]]
- Solo i capi prelevati fisicamente da una Zona Morta e conformi a soglie minime di bounding box (giacche, pantaloni, maglieria > €40-50) generano un tracker attivo.

### 4. Action Recognition Selettivo
- L'analisi cinematica e di posa si attiva **esclusivamente sulla ROI di intersezione** tra la persona e il capo vivo.

### 5. Validazione Temporale
- Verifica sequenziale a timer (10s) gestita dalla [[logica-booleana-allarme]] per assorbire occlusioni temporanee legittime.

---

## Vantaggi Chiave

- **Riduzione del carico computazionale del 95%+**: L'action recognition viene eseguita solo su poche bounding box per frame anziché sull'intera scena.
- **Zero dipendenza da Scene Understanding neurale complesso**: Le geometrie del negozio sono fornite a costo zero tramite GUI.
- **Robusta contro i falsi positivi**: Il filtro dimensionale e l'esclusione dell'ingresso eliminano indumenti personali e piccoli accessori.

---

## Fonti

- [[architettura-flusso-sequenziale]] — Sezione Principi Architetturali e Flusso a 5 Fasi

---

*Pagina creata da ingestione di [[architettura-flusso-sequenziale]]*
