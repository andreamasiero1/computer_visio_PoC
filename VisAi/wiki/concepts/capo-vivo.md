---
title: "Capo Vivo (Tracciamento Selettivo del Prodotto)"
type: concept
created: 2026-08-19
updated: 2026-08-19
tags: [capo-vivo, object-tracking, computer-vision, bounding-box, retail-security, edge-ai]
domain: "Computer Vision"
complexity: intermediate
confidence: high
related: ["[[cascade-funnel-pipeline]]", "[[action-recognition]]", "[[logica-booleana-allarme]]", "[[object-counting]]"]
---

# 🏷️ Capo Vivo (Tracciamento Selettivo del Prodotto)

> Stato dinamico assegnato a un capo di abbigliamento quando viene prelevato da uno scaffale o appendiabiti, diventando l'unico target attivo per i modelli di Action Recognition.

---

## Definizione

Nel sistema VisAi, su un inventario di centinaia o migliaia di capi esposti in negozio, la quasi totalità rimane statica su stand e grucce. 
Un bounding box di abbigliamento viene promosso allo stato di **"Capo Vivo"** se e solo se soddisfa contemporaneamente due condizioni vincolanti:

1. **Soglia Dimensionale / Valore (Filtro Anti-Rumore)**:
   - Il bounding box supera una soglia minima di area in pixel (escludendo piccoli accessori come calzini, gioielli, foulard o cinture).
   - Target di mercato: capi di valore medio-alto (> €40–50, come giacche, felpe, maglioni, pantaloni).
2. **Origine da Zona Morta (Provenienza Certificata)**:
   - Il movimento del capo ha origine all'interno di una delle **Zone Morte** configurate via GUI (es. sfilato da una gruccia o prelevato da uno scaffale).
   - I capi portati in mano dai clienti dall'ingresso del negozio **non** originano da una zona morta, quindi non diventano mai Capi Vivi.

---

## Ciclo di Vita del Capo Vivo

```
[ Capo Statico in Zona Morta ]
              │
              ▼ (Prelevato dal cliente + Dimensioni idonee)
      [ CAPO VIVO CREATO ]
              │
              ├──► [ Tracciato continuamente assieme alla Persona ]
              │
              ▼ (Gesto sospetto rilevato in Fase 4)
  [ Capo Vivo Scompare dalla Vista ]
              │
              ├── Se ricompare entro 10s ──► Reset Timer & Prosegue Tracking
              └── Se NON ricompare entro 10s ──► ALLARME CONFERMATO (Occultamento)
```

---

## Vantaggi Architetturali

- **Ottimizzazione delle Risorse**: Il Multi-Object Tracking (MOT) e la correlazione con le persone sono concentrati solo sui pochissimi capi effettivamente movimentati (spesso 1–3 per volta per telecamera).
- **Immunità da Oggetti Personali**: Impedisce di lanciare allarmi o spendere cicli GPU per cappotti, sciarpe o borse personali già in possesso del cliente.

---

## Fonti

- [[architettura-flusso-sequenziale]] — Fase 3: Verifica Capo fuori Zona Morta [CREAZIONE CAPO VIVO]

---

*Pagina creata da ingestione di [[architettura-flusso-sequenziale]]*
