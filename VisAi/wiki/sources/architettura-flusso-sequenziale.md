---
title: "Architettura e Logica del Flusso Sequenziale (VisAi)"
type: source
source_type: note
created: 2026-08-19
updated: 2026-08-19
tags: [architettura, pipeline, cascade-funnel, capo-vivo, action-recognition, edge-ai, retail-security, privacy]
sources: ["VisAi/raw/notes/architettura-flusso-sequenziale.md"]
author: "Andrea Masiero"
confidence: high
related: ["[[cascade-funnel-pipeline]]", "[[capo-vivo]]", "[[logica-booleana-allarme]]", "[[action-recognition]]", "[[edge-ai]]", "[[computer-vision-retail-security]]"]
---

# 📄 Architettura e Logica del Flusso Sequenziale (VisAi)

> Documento di riferimento tecnico per la pipeline di elaborazione video, tracciamento capi attivi, riconoscimento azioni e innesco allarmi per il sistema VisAi.

---

## Riassunto

Il documento formalizza l'architettura a imbuto (**Cascade Funnel**) di VisAi. L'obiettivo primario è rendere computazionalmente sostenibile l'elaborazione video in real-time su hardware **Edge AI** locale, riducendo drasticamente i falsi positivi grazie a rigide regole di business e di dominio fisico.

La pipeline è strutturata in **5 fasi strettamente sequenziali**, integrando logiche deterministiche (GUI per zone morte, filtri dimensionali) con modelli neurali (Person Detection, Pose Estimation, Action Recognition) attivati solo on-demand.

---

## Principi Architetturali e Regole di Dominio

| Regola / Principio | Dettaglio Operativo | Obiettivo |
|---|---|---|
| **GUI Zone Morte** | Scaffali e rack vengono delimitati via GUI dall'operatore umano in fase di setup. | Zero overhead AI per lo scene understanding strutturale. |
| **Esclusione Cestini** | Target circoscritto a retail senza shopping bag/cestini. | Eliminazione della causa primaria di occlusione legittima. |
| **Filtro Dimensione/Valore** | Tracciamento solo di capi rilevanti (> €40-50, es. giacche, maglie, pantaloni). | Esclusione piccoli accessori rumorosi (calzini, cinture). |
| **Esclusione Ingresso** | L'ingresso negozio non è mappato come zona morta. | Nessun falso allarme per indumenti personali portati dall'esterno. |

---

## Sintesi del Flusso a 5 Fasi

1. **Fase 1: Preprocessing & Mascheramento**
   - *1.1 Zone Morte*: Mascheramento computazionale dei capi fermi su rack/scaffali.
   - *1.2 Face Blurring*: Oscuramento volti immediato a inizio pipeline (Privacy by Design, GDPR, EU AI Act).
2. **Fase 2: Person Detection & Spazializzazione**
   - Rilevamento bounding box persone per mappare la loro posizione (es. corsia generica vs area alto valore).
3. **Fase 3: Transizione "Capo Vivo"**
   - Un capo d'abbigliamento diventa **Capo Vivo** solo se supera la soglia dimensionale e la sua traiettoria parte da una Zona Morta.
4. **Fase 4: Riconoscimento Gesto Sospetto**
   - Modelli complessi (Pose Estimation / Action Recognition / Analisi Cinematica) eseguiti **esclusivamente** sull'intersezione tra la Persona e il Capo Vivo.
5. **Fase 5: Timer di Validazione (Doppia Verifica 10s)**
   - Se il Capo Vivo scompare dopo un gesto sospetto, un timer di 10 secondi attende la sua ricomparsa. Se non ricompare entro 10s e le mani sono vuote, l'allarme viene confermato.

---

## Equazione di Allarme

$$\text{Allarme} = (\text{CapoVivo} = \text{TRUE}) \land (\text{GestoSospetto} = \text{TRUE}) \land (\text{Ricomparsa}_{10s} = \text{FALSE})$$

---

## Key Takeaways

- **Cascade Funnel**: L'AI pesante si attiva solo all'ultimo stadio e su una frazione minima dei pixel (intersezione Persona-Capo Vivo).
- **Privacy by Design**: Il Face Blurring in testata garantisce conformità immediata al GDPR e all'EU AI Act prima di qualunque analisi a valle.
- **Determinismo + AI**: La combinazione di mascheramento statico da GUI e filtri dimensionali scarica l'Edge server dal 95%+ del carico computazionale.
- **Tolleranza Occlusioni**: Il timer di 10 secondi nella Fase 5 evita i falsi allarmi causati da rotazioni corporee o occlusioni temporanee innocue.

---

## Pagine wiki collegate

- **Concetti**: [[cascade-funnel-pipeline]], [[capo-vivo]], [[logica-booleana-allarme]], [[action-recognition]], [[edge-ai]]
- **Topic**: [[computer-vision-retail-security]]

---

*Pagina creata da ingestione #5 — 2026-08-19*
