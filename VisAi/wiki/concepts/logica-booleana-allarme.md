---
title: "Logica Booleana di Allarme e Doppia Verifica Temporale"
type: concept
created: 2026-08-19
updated: 2026-08-19
tags: [allarme, logica-booleana, false-positive-reduction, action-recognition, capo-vivo, timer-validation]
domain: "Computer Vision / Decision Logic"
complexity: intermediate
confidence: high
related: ["[[cascade-funnel-pipeline]]", "[[capo-vivo]]", "[[action-recognition]]", "[[edge-ai]]", "[[computer-vision-retail-security]]"]
---

# 🧠 Logica Booleana di Allarme e Doppia Verifica Temporale

> Meccanismo di validazione sequenziale e temporale a doppia verifica per confermare i furti ed eliminare i falsi positivi causati da occlusioni corporee momentanee.

---

## L'Equazione Booleana

L'innesco dell'alert definitivo per lo staff (notifica app o avviso sonoro discreto) avviene solo e soltanto quando tre condizioni temporali e spaziali risultano vere in sequenza:

```text
Allarme = (Esiste CapoVivo == TRUE) 
          AND (GestoSospetto Rilevato == TRUE) 
          AND (CapoVivo Ricomparso entro 10s == FALSE)
```

---

## Dettaglio dei Termini

### 1. `Esiste CapoVivo == TRUE`
- Il capo deve essere stato prelevato da uno scaffale o appendiabiti configurato come Zona Morta e deve rispettare i parametri dimensionali minimi.
- Se l'azione viene eseguita su un capo portato dall'esterno o su un piccolo accessorio non tracciato, la condizione è `FALSE`.

### 2. `GestoSospetto Rilevato == TRUE`
- I modelli di Action Recognition / Analisi Cinematica rilevano un pattern cinematico anomalo (es. movimento del braccio verso una tasca interna, una giacca o uno zaino aperto) circoscritto all'intersezione tra la Persona e il [[capo-vivo]].

### 3. `CapoVivo Ricomparso entro 10s == FALSE` (Doppia Verifica)
- **Problema di dominio**: Il cliente potrebbe semplicemente girarsi di schiena, coprire temporaneamente il capo con il busto o metterlo sotto il braccio per osservare un altro articolo.
- **Risoluzione a Timer**:
  - Nel momento in cui scatta il flag di gesto sospetto e il Capo Vivo scompare dalla visuale della telecamera, parte un timer di **10 secondi**.
  - **Caso Positivo (Occultamento confermato)**: Il timer scade (10s), il Capo Vivo non è più visibile e le mani del cliente risultano vuote $\rightarrow$ Allarme **TRIGGERATO**.
  - **Caso Falso Allarme (Occlusione innocua)**: Il cliente si rigira o mostra nuovamente il capo prima dei 10 secondi $\rightarrow$ Timer **RESETTATO** e allarme annullato.

---

## Tabella di Verità e Risoluzione Casi

| Esiste Capo Vivo? | Gesto Sospetto? | Capo Ricomparso nei 10s? | Esito Sistema | Spiegazione Operativa |
|:---:|:---:|:---:|:---:|---|
| ❌ FALSE | — | — | **No Allarme** | Oggetto personale o rumore visivo ignorato. |
| ✅ TRUE | ❌ FALSE | — | **No Allarme** | Normale interazione con i prodotti in esposizione. |
| ✅ TRUE | ✅ TRUE | ✅ TRUE (Ricomparso) | **No Allarme** (Reset) | Falso allarme: occlusione temporanea dal corpo del cliente. |
| ✅ TRUE | ✅ TRUE | ❌ FALSE (Non ricomparso) | 🚨 **ALLARME ATTIVO** | Occultamento intenzionale confermato con doppia verifica. |

---

## Fonti

- [[architettura-flusso-sequenziale]] — Sezione Logica Booleana di Allarme e Fase 5

---

*Pagina creata da ingestione di [[architettura-flusso-sequenziale]]*
