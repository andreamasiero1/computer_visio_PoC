# Rielaborazione Commentata — Flusso Operativo [1] GuardIA/VisAi

---

## 📸 Screen 1 — Flusso Operativo Sequenziale (Step 0→4)

### Mia rielaborazione

Il flusso è pensato come una **pipeline rigidamente sequenziale** (ogni step dipende dal precedente) composta da 5 fasi numerate 0→4:

---

#### Step 0 — Prerequisiti Infrastrutturali
- **Switching multi-camera**: l'AI deve operare su più telecamere contemporaneamente e gestire la continuità di tracking di persone e capi attraverso i feed video di diverse cam.
- **Creazione delle 3 zone semantiche** (definite nel dettaglio nello screen 4):
  - **Zona Morta** → punti di esposizione/racks + cassa
  - **Zona Nera** → ingressi/uscite + corridoi di passaggio
  - **Zona Persa** → bordi dell'inquadratura che danno su aree non coperte da telecamere
- **Blur facce** → anonimizzazione immediata all'input per compliance GDPR/AI Act.

> **Mio commento**: Lo step 0 è correttamente posizionato come precondizione. La suddivisione in 3 zone è un'evoluzione rispetto al modello originale che aveva solo "zone morte" e un generico "fuori zona". L'introduzione della **Zona Persa** è una scelta pragmatica e intelligente per gestire la realtà dei negozi con copertura parziale (anche solo 50%). La **Zona Nera** come gateway di controllo dedicato agli ingressi/uscite è un'aggiunta critica che prima era implicita.

---

#### Step 1 — Riconoscimento Persone
- Creazione del **bounding box persona** su ogni individuo rilevato.
- **Associazione persona ↔ zona del negozio** tramite mapping camera-zona (cam 1 == zona 1).

> **Mio commento**: L'associazione diretta cam→zona è semplice e funzionale. Presuppone che ogni camera abbia un campo visivo che corrisponde a una zona precisa. Funziona bene se le zone non si sovrappongono eccessivamente tra le inquadrature di cam diverse. Il punto è: **la persona viene tracciata, il capo no — non ancora**. Si crea prima il "contenitore" (persona), poi si cerca il "contenuto" (capo vivo).

---

#### Step 2 — Monitoraggio Capo Fuori Zona Morta → Nascita del "Capo Vivo"
- Un capo che si muove **fuori da una zona morta** viene riquadrato come **Capo Vivo**.
- **2.1**: Si classifica il capo vivo per **tipo** (scarpa/pantalone/maglia) e **colore**.
- **2.2**: Si definisce **vagamente** la persona associata al capo vivo tramite caratteristiche visive non biometriche: colore del giubbotto/giacca sgargiante, cappello, sciarpa, occhiali, ecc. *(nota: "da ragionare" — punto ancora aperto)*.

> **Mio commento**: Questo step è il cuore del "Cascade Funnel". Tra le migliaia di capi statici in negozio, l'AI attiva tracking solo su quelli che si separano dalle zone morte. È il filtro computazionale più importante. La caratterizzazione al punto 2.2 è un mini-sistema di **Re-Identification leggero e privacy-preserving**: non usi la faccia, ma attributi visivi grossolani per mantenere l'identità della persona attraverso i frame. Il "da ragionare" al punto 2.2 è onesto — il livello di dettaglio di questa caratterizzazione è un trade-off delicato tra efficacia del Re-ID e carico computazionale.

---

#### Step 3 — Due Scenari Paralleli (3.a e 3.b)

**3.a — Gesto Sospetto (nucleo anti-taccheggio)**:
- L'AI esegue riconoscimento gesti **SOLO** sull'intersezione Persona ∩ Capo Vivo.
- Condizione di trigger: **movimento specifico + riquadro capo vivo che scompare** (= il capo viene occultato sul corpo della persona).

**3.b — Capo Vivo Fuori Inquadratura**:
- L'AI rileva che un **cliente esce dall'inquadratura portando con sé un capo vivo**.
- Non è necessariamente sospetto, ma richiede tracking e gestione (dipende dalla zona verso cui esce — dettagliato nello screen 4).

> **Mio commento**: La biforcazione 3.a/3.b è logicamente necessaria e ben ragionata. Il 3.a copre il caso classico (occultamento fisico del capo), il 3.b copre il caso strutturale (uscita dal campo visivo con il capo in mano, che in uno scenario di copertura al 50% sarà **molto frequente**). Notare che 3.b NON è automaticamente un allarme alto — diventa allarme massimo solo se l'uscita avviene dalla **Zona Nera** (= uscita dal negozio).

---

#### Step 4 — Validazione Temporale (10 secondi)
- Dopo un flag al punto 3.a: se il capo vivo **NON ricompare entro 10 secondi** → allarme confermato.
- Se ricompare → falso positivo, reset.

> **Mio commento**: Il timer a 10s è il filtro anti-falso-positivo finale. Copre le occlusioni temporanee innocue (persona che si gira, capo momentaneamente nascosto dal corpo, posa il capo su un banco per guardarlo, ecc.). È un meccanismo elegante e a costo computazionale quasi zero.

---

## 📸 Screen 2 — Scenari di Allarme e Logica Booleana

### Mia rielaborazione

Il sistema produce **3 livelli di priorità di segnalazione**:

| Priorità | Trigger | Azione |
|----------|---------|--------|
| **ALTA** (3.a confermato) | `CapoVivo == TRUE AND GestoSospetto == TRUE AND Ricomparso[10s] == FALSE` | Segnalazione + **intervento immediato** del personale (deterrenza) |
| **MEDIA** (Limite 1) | Capo vivo scompare per sovrapposizione e non riappare in 20/30s | Segnalazione con tipo capo + persona (per controllo commessi) |
| **BASSA** (3.b) | Persona esce dall'inquadratura con capo vivo (verso zona persa) | Segnalazione con tipo capo + persona (per controllo commessi) |

**Nota critica dal documento**: Anche in scenario 3.b (priorità bassa), il flusso completo fino al punto 4 deve comunque essere eseguito — non si salta la verifica dei 10 secondi.

> **Mio commento**: La gerarchia a 3 livelli è ben pensata dal punto di vista operativo per il personale. Non ogni segnalazione richiede un intervento d'emergenza — le priorità media e bassa servono come **intelligence passiva** per i commessi, che possono verificare in modo naturale (avvicinarsi al cliente, offrire assistenza). Questo riduce lo stress operativo e i "falsi allarmi percepiti" dal personale, che è un problema reale nei sistemi anti-taccheggio tradizionali.

> A questo si aggiunge il **MASSIMO ALLARME** dalla Zona Nera (screen 4): persona che esce dalla zona nera con un capo vivo. Questo è il livello più alto possibile — il cliente sta uscendo dal negozio con merce non pagata.

---

## 📸 Screen 3 — Limite 1: Falsa Scomparsa per Sovrapposizione

### Mia rielaborazione

**Il problema**: Tra lo step 2 e lo step 3, il riquadro del capo vivo potrebbe scomparire **senza che sia avvenuto un gesto sospetto**, a causa di:
- Sovrapposizione tra **due capi vivi** (un capo ne nasconde un altro)
- Sovrapposizione tra **persona e capo vivo** (il corpo della persona occlude il capo)
- Sovrapposizione tra **due persone** (una persona nasconde l'altra che tiene il capo)

**La soluzione proposta**: 
1. L'AI **congela l'ultima posizione nota** del riquadro del capo vivo.
2. Parte un **timer di ricerca di 20/30 secondi** (più lungo dei 10s della verifica standard — questo è importante).
3. Durante il timer, l'AI cerca nelle **strette vicinanze** un capo con le **stesse caratteristiche** (colore + tipologia) nelle mani dello stesso cliente o di un diverso cliente nelle vicinanze.
4. Se il capo viene **ri-trovato come capo vivo nelle mani di qualcuno** → ripresa tracking, nessun allarme.
5. Se il capo viene **trovato come "capo morto" in zona viva** (= è stato posato su un punto che non è una zona morta, tipo un tavolo, una sedia, per terra) → potenziale anomalia.
6. Se il capo **non viene ritrovato affatto** entro 20/30s → **PRIORITÀ MEDIA**: segnalazione con tipo capo + persona.

> **Mio commento**: Questa soluzione è solida e affronta il problema più realistico in un negozio affollato. Il timer di 20/30s (più lungo del timer standard di 10s) dà margine sufficiente per le occlusioni temporanee da folla. Il concetto di "ricerca per attributi visivi" (colore + tipo) nelle vicinanze è computazionalmente più pesante della semplice verifica di ricomparsa al punto 4, ma è applicato solo in un caso specifico e localizzato, quindi il carico aggiuntivo è gestibile. Il downgrade a priorità MEDIA anziché ALTA è sensato: non c'è stata evidenza di gesto sospetto, solo una perdita di tracking.

---

## 📸 Screen 4 — Limite 3: Capo Preso da Zona Morta Fuori Inquadratura

### Mia rielaborazione

**Il problema (contestualizzato dalla tua info aggiuntiva)**: In negozi con copertura video parziale (anche solo 50%), esistono zone morte **non coperte da nessuna telecamera**. Un cliente può prendere un capo da un rack in una di queste zone non coperte e poi entrare nell'inquadratura **già con il capo in mano**. L'AI non ha mai "visto" il capo lasciare una zona morta, quindi non lo ha mai classificato come Capo Vivo. Senza soluzione, questo capo sfugge completamente al sistema.

**La soluzione: Architettura a 3 Zone**

### 1. ZONA MORTA
- **Dove**: Punti di esposizione abiti (racks, scaffali, appendini) visibili dentro l'inquadratura + area cassa.
- **Compito**: 
  - **Genera** il Capo Vivo quando un capo si allontana dalla zona.
  - **Elimina silenziosamente** il riquadro Capo Vivo quando un capo vi rientra (= il capo è stato rimesso a posto o è stato pagato in cassa). Nessuna segnalazione.

> **Mio commento sulla Zona Morta**: La funzione duale genera/elimina è logica. L'inclusione della **cassa** nella zona morta è elegante: quando un cliente porta un capo in cassa, il capo vivo viene eliminato automaticamente — il pagamento "neutralizza" il capo senza bisogno di integrazioni con il POS. Tuttavia, questo introduce un rischio che analizzo più avanti nei limiti aggiuntivi.

### 2. ZONA NERA
- **Dove**: Ingressi/uscite del negozio, **ed anche i corridoi di passaggio**. Compatibile con le zone morte e la zona viva. Obiettivo: **PIÙ GRANDE È MEGLIO È**.
- **Compiti** (logica direzionale rispetto all'interno del negozio):
  - **IN ENTRATA alla zona nera** (= persona entra nel negozio): Creazione del riquadro persona. Essenzialmente lo step 1 del flusso.
  - **IN USCITA dalla zona nera** (= persona esce dal negozio):
    - Con Capo Vivo → **MASSIMO ALLARME**
    - Senza riquadro capo → **Normalità**

> **Mio commento sulla Zona Nera**: Questa è la **barriera definitiva**. È il perimetro dove avviene la decisione binaria finale: paghi o rubi. La logica "più grande è meglio è" ha senso perché una zona nera ampia aumenta il tempo in cui l'AI può analizzare la persona prima che varchi l'uscita, dando più frame per la conferma. L'inclusione dei **corridoi di passaggio** nella zona nera è interessante — sembra servire a massimizzare le zone dove la persona è tracciata con bounding box, anche se non sono propriamente uscite.

### 3. ZONA PERSA
- **Dove**: Bordi dell'inquadratura delle telecamere che affacciano su aree **interne al negozio ma non coperte da alcuna cam**.
- **Compiti** (logica direzionale):
  - **IN USCITA dalla zona persa** (= persona entra nella zona non coperta):
    - Con Capo Vivo → **Scenario 3.b** (priorità bassa, segnalazione con tipo capo + persona)
    - Senza riquadro capo → **Normalità**
  - **IN ENTRATA dalla zona persa** (= persona rientra in inquadratura dalla zona non coperta):
    - L'AI **analizza le mani** della persona per verificare se porta con sé un capo del negozio.
    - **[Scelta 1]**: Se riconosce un Capo Vivo → **CREA RIQUADRO** (il capo viene "registrato" nel sistema come capo vivo per la prima volta).
    - Senza capo → **Normalità**

> **Mio commento sulla Zona Persa**: Questa è la soluzione più innovativa e anche la più sfidante dal punto di vista tecnico. L'analisi delle **mani** per riconoscere un capo del negozio al rientro dalla zona non coperta è concettualmente corretta, ma è il task di computer vision più difficile dell'intero flusso. La notazione **"[scelta 1]"** suggerisce che esistono alternative ancora in valutazione — vedi le mie domande sotto.

---

## ⭐ Valutazione Complessiva del Servizio

### Punti di Forza

| Aspetto | Valutazione |
|---------|------------|
| **Architettura a Funnel** | Eccellente. Ogni step riduce drasticamente il carico computazionale per lo step successivo. L'AI pesante (gesture recognition) si attiva solo sul sottoinsieme minimo necessario. |
| **Pragmatismo commerciale** | Molto buono. Il sistema è progettato per la realtà (copertura 50%, non 100%), non per il caso ideale. Questo lo rende deployabile subito. |
| **Gerarchia 3 livelli di allarme** | Buono. Evita l'"alarm fatigue" del personale differenziando le priorità. Il commesso sa cosa richiede azione immediata e cosa richiede solo attenzione. |
| **Privacy by Design** | Eccellente. Blur facce al punto 0, Re-ID basato su attributi non biometrici. Compliance nativa GDPR + AI Act. |
| **Logica booleana chiara** | Buono. La formula `CapoVivo AND GestoSospetto AND NOT Ricomparso[10s]` è limpida, verificabile, spiegabile anche a un auditor. |
| **Zona Persa come concetto** | Innovativo. Anziché ignorare le zone non coperte, le gestisce attivamente come "frontiere" con logica direzionale. |

### Punti di Attenzione

| Aspetto | Commento |
|---------|----------|
| **Analisi mani in zona persa** | È il componente tecnicamente più rischioso. La detection di oggetti nelle mani in condizioni reali (illuminazione variabile, occlusione parziale, garment piegato) ha accuracy limitata. |
| **Re-ID persona cross-camera** | Il flusso presuppone switching tra telecamere ma non dettaglia come l'identità della persona viene mantenuta da una cam all'altra. |
| **Caratterizzazione persona (2.2)** | Il "da ragionare" è un debito progettuale aperto. Troppo poco dettaglio = Re-ID fallisce; troppo dettaglio = carico computazionale e rischi privacy. |

---

## 🚨 Limiti Aggiuntivi Individuati

### Limite A — Cassa come Zona Morta: Rischio di "Bypass Silenzioso"

La cassa è classificata come zona morta, il che significa che **qualsiasi capo vivo che entra nella zona cassa viene eliminato senza segnalazione**. Ma:
- Cosa succede se un cliente **passa vicino/attraverso la zona cassa senza pagare** e il capo vivo viene erroneamente eliminato?
- In un negozio con zona cassa ampia o non ben delimitata fisicamente, un passaggio laterale potrebbe "azzerare" il tracking del capo.

Possibile contromisura: la zona morta della cassa potrebbe avere una logica diversa dalle zone morte degli espositori — ad esempio, richiedere **un tempo di permanenza minimo** del capo in zona cassa prima di eliminarlo (il pagamento richiede tempo, il passaggio laterale no).

---

### Limite B — Re-Identification Cross-Camera

Lo step 0 dichiara come essenziale la capacità di switching tra telecamere. Ma quando una persona esce dal campo della cam 1 ed entra nel campo della cam 2:
- Come viene mantenuta la **continuità dell'identità persona**?
- Come viene mantenuta la **continuità del capo vivo associato** a quella persona?

Con la caratterizzazione "vaga" del punto 2.2 (colore giacca, cappello, sciarpa...), il Re-ID è fattibile ma fragile. In un negozio con molti clienti vestiti in modo simile, si rischia di **scambiare persone** e associare un capo vivo alla persona sbagliata.

---

### Limite C — Passaggio del Capo tra Complici

Il flusso traccia la coppia (persona, capo vivo). Ma un classico scenario di furto organizzato prevede:
1. Persona A prende il capo dalla zona morta → diventa capo vivo associato a Persona A.
2. Persona A **passa il capo a Persona B** (in modo naturale, come una conversazione tra "amici").
3. Persona B occultà il capo. Persona A esce senza capo. Persona B esce senza che il sistema abbia associato il capo a lei.

Il Limite 1 (sovrapposizione tra persone) copre parzialmente questo scenario, ma non esplicitamente il **passaggio deliberato e cooperativo**.

---

### Limite D — Capo Vivo Modificato Visivamente

Un taccheggiatore esperto potrebbe:
- **Rovesciare** il capo (interno vs. esterno cambia colore)
- **Piegarlo** strettamente (cambia forma/dimensioni)
- **Infilarlo sotto il proprio capo** parzialmente

In questi casi, il Re-ID basato su "colore + tipologia" del capo potrebbe fallire: l'AI vede un capo con attributi diversi e non lo riconosce come il capo vivo originale, interpretandolo come una scomparsa.

---

### Limite E — Gestione dei Timer Multipli in Simultanea

In uno scenario con 5-10 clienti attivi, è possibile che si attivino **contemporaneamente**:
- Timer di 10s del punto 4 per un cliente
- Timer di 20/30s del Limite 1 per un altro cliente
- Tracking zona persa per un terzo

Il flusso è descritto come sequenziale, ma l'esecuzione reale è **parallela e multi-target**. Non è chiaro come vengono gestiti conflitti di risorse computazionali quando più flussi sono attivi contemporaneamente.

---

### Limite F — Scarpa come Capo Vivo

Al punto 2.1, "scarpa" è elencata come tipo di capo vivo. Tuttavia:
- Le scarpe vengono **provate in modo diverso** dagli altri capi — il cliente si siede, si toglie le proprie, le prova. Questo genera un pattern gestuale radicalmente diverso da giacche/maglioni.
- Le scarpe vengono tipicamente esposte **una sola, non in coppia** — l'AI dovrebbe tracciare un singolo item di dimensioni molto diverse da un capo d'abbigliamento.
- Il **gesto sospetto** per occultare una scarpa (metterla in uno zaino) è molto diverso dal gesto per occultare una giacca (indossarla sotto la propria).

Serve un modello di gesture recognition specifico o la detection di scarpe va gestita con logiche differenti?

---

## ❓ Domande di Chiarimento

### Domanda 1 — Limite 2 mancante
Nello screen 3 vedo **Limite 1**, nello screen 4 vedo **Limite 3**. Il **Limite 2** non è stato allegato o non esiste ancora? Se esiste, me lo puoi condividere?

### Domanda 2 — "[Scelta 1]" nella Zona Persa
Nella logica della zona persa (screen 4), quando una persona rientra in inquadratura, la soluzione di analizzare le mani è indicata come **"[scelta 1]"**. Questo implica che esistono **altre scelte/alternative** valutate? Se sì, quali sono?

### Domanda 3 — "Scargiante" al punto 2.2
Al punto 2.2, il termine "scargiante" lo interpreto come **"sgargiante"** (colore vivace/acceso del giubbotto). È un **esempio di attributo** o è l'**unico tipo di colore** che viene registrato? Cioè: se il cliente ha una giacca grigia anonima, quali attributi si usano per il Re-ID?

### Domanda 4 — Zona Morta della Cassa vs. Zona Morta degli Espositori
La **cassa e gli espositori** sono entrambi zona morta con lo stesso comportamento (elimina capo vivo senza segnalazione). Ma la cassa ha una semantica operativa diversa (pagamento). Avete ragionato sulla possibilità di **differenziare** il comportamento della zona morta in base al tipo (espositore vs. cassa)?

### Domanda 5 — Cosa è un "Capo Morto in Zona Viva"?
Nel Limite 1 (screen 3), si menziona il caso in cui il capo scomparso viene "riconosciuto come **capo morto** IN ZONA VIVA". Questo significa che l'AI vede il capo posato su una superficie che **non è** una zona morta (tipo un tavolo, una panchina, il pavimento)? E in quel caso, cosa succede — si elimina il riquadro? Si genera una segnalazione? Il testo non lo dettaglia.

### Domanda 6 — Direzione nella Zona Nera
La zona nera ha logica **direzionale** (in entrata = crea persona, in uscita = check allarme). Come viene determinata la **direzione** di movimento rispetto al "dentro" e "fuori" del negozio? È basata sulla posizione relativa della zona nera nell'inquadratura (es. lato sinistro = entrata, lato destro = uscita) o su un'analisi del vettore di movimento della persona?
