# Architettura e Logica del Flusso Sequenziale (VisAi)

> Documento di riferimento per la pipeline di elaborazione video, riconoscimento azioni e innesco allarmi del sistema VisAi.

## 📌 Principi Architetturali e Regole di Dominio
Il sistema si basa su un'architettura a imbuto (Cascade Funnel) che riduce drasticamente il carico computazionale (Edge AI) e minimizza i falsi positivi restringendo il dominio operativo attraverso regole di business ferree:
- **GUI Zone Morte:** Le zone morte (scaffali, rack) sono definite deterministicamente dal personale tramite interfaccia grafica. Nessun calcolo AI è richiesto per lo scene understanding strutturale.
- **Esclusione Cestini:** Il target sono catene retail che NON utilizzano shopping bags o cestini, rimuovendo la principale causa di occlusione legittima.
- **Filtro Valore/Dimensione:** Vengono tracciati solo capi di dimensioni rilevanti (target €40-50+ come giacche, maglie, pantaloni), escludendo piccoli accessori (es. calzini) che generano rumore visivo.
- **Esclusione Ingresso:** L'ingresso del negozio non è mappato come zona morta, impedendo al sistema di attivare il tracciamento sui capi personali portati in mano dai clienti dall'esterno.

---

## ⚙️ Il Flusso a 5 Fasi

### Fase 1. Switching riquadro camera tramite AI
- **1.1 Zone morte:** Mascheramento computazionale delle aree in cui risiedono i capi fermi (rack/scaffali).
- **1.2 Blur facce:** Oscuramento immediato e preventivo dei volti in testa alla pipeline per garantire la compliance alla normativa GDPR / EU AI Act (Privacy by Design).

### Fase 2. Riconoscimento persone in determinata situazione
- **Meccanica:** Estrazione dei Bounding Box delle persone (Person Detection).
- **Obiettivo:** Mappare la posizione spaziale della persona all'interno delle aree del negozio (es. corsia generica vs. area capi di alto valore) per fornire contesto ai modelli successivi.

### Fase 3. Verifica Capo fuori Zona Morta [CREAZIONE CAPO VIVO]
- **Meccanica:** Un Bounding Box di abbigliamento viene classificato e tracciato come **"Capo Vivo"** se e solo se: 
  1. Supera la soglia dimensionale (no piccoli accessori).
  2. Il suo movimento ha origine da una Zona Morta definita in Fase 1 (es. viene sfilato da una gruccia).
- **Vantaggio Computazionale:** Il tracciamento non viene eseguito sui 500 capi presenti nel negozio, ma esclusivamente sui pochissimi capi fisicamente nelle mani dei clienti in quel momento.

### Fase 4. Riconoscimento Gesto Sospetto [SOLO SU CAPO VIVO]
- **Meccanica:** I modelli computazionalmente pesanti (Pose Estimation / Action Recognition / Analisi Cinematica) si attivano **soltanto** sull'intersezione tra la Persona e il Capo Vivo. 
- **Trigger:** L'algoritmo rileva movimenti del braccio/corpo che suggeriscono occultamento (es. spingere il capo vivo verso l'interno di una giacca, uno zaino o una tasca).

### Fase 5. Riquadro Capo Vivo ricomparso nei 10 sec (Doppia Verifica)
- **Meccanica:** Step *strettamente sequenziale*. Si attiva esclusivamente se la Fase 4 ha rilevato un Gesto Sospetto. Funziona come timer di validazione per tollerare le occlusioni corporee legittime.
- **Logica:** Dal momento in cui scatta il flag della Fase 4, se il Capo Vivo scompare dalla vista (es. il cliente si gira di schiena) e **non ricompare entro 10 secondi** con le mani vuote, l'occultamento è confermato.
- **Risoluzione falsi positivi:** Se l'azione della Fase 4 era innocua (falso allarme) e l'oggetto era solo nascosto dal corpo, riapparendo entro 10 secondi il timer viene resettato e l'allarme annullato.

---

## 🧠 Logica Booleana di Allarme

Il sistema innesca l'alert finale (Notifica Staff / Intervento Attivo) solo quando si verifica la seguente equazione rigorosa in sequenza temporale:

```text
Allarme = (Esiste CapoVivo == TRUE) 
          AND (GestoSospetto Rilevato == TRUE) 
          AND (CapoVivo Ricomparso entro 10s == FALSE)
```
