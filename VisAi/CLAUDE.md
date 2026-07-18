# CLAUDE.md — LLM Wiki Schema

> Questo file è lo schema operativo della wiki. Ogni sessione di lavoro inizia leggendo questo file.
> L'LLM lo segue come un contratto. L'utente e l'LLM lo co-evolvono nel tempo.

---

## 1. Architettura

```
VisAi/
├── CLAUDE.md              ← Questo file: schema e regole
├── raw/                   ← Fonti grezze (immutabili, l'LLM NON le modifica mai)
│   ├── articles/          ← Articoli web clippati
│   ├── papers/            ← Paper accademici, PDF convertiti
│   ├── notes/             ← Appunti personali, journal entries
│   ├── transcripts/       ← Trascrizioni di meeting, podcast, video
│   └── assets/            ← Immagini, allegati, file binari
├── wiki/                  ← Wiki generata dall'LLM (l'LLM possiede questo layer)
│   ├── index.md           ← Catalogo di tutte le pagine, per categoria
│   ├── log.md             ← Log cronologico di tutte le operazioni
│   ├── overview.md        ← Panoramica generale della knowledge base
│   ├── sources/           ← Schede riassuntive di ogni fonte ingerita
│   ├── entities/          ← Pagine entità (persone, aziende, strumenti, luoghi)
│   ├── concepts/          ← Pagine concetto (teorie, framework, pattern)
│   ├── topics/            ← Pagine topic (aree tematiche ampie)
│   ├── analyses/          ← Analisi, confronti, sintesi generate da query
│   └── meta/              ← Pagine meta (contradizioni, gap, TODO della wiki)
```

### Tre layer

| Layer | Proprietario | Mutabilità | Scopo |
|-------|-------------|------------|-------|
| `raw/` | Utente | Immutabile (append-only) | Fonti grezze, verità di base |
| `wiki/` | LLM | L'LLM crea, aggiorna, elimina | Conoscenza compilata e interlinkata |
| `CLAUDE.md` | Utente + LLM | Co-evoluto | Regole, convenzioni, workflow |

---

## 2. Convenzioni per i file

### 2.1 Naming

- **Fonti (`raw/`)**: nome descrittivo, lowercase, trattini: `raw/articles/come-funziona-rag.md`
- **Pagine wiki (`wiki/`)**: lowercase, trattini, niente spazi: `wiki/entities/openai.md`
- **Nessun carattere speciale** nei nomi file (no accenti, no parentesi)

### 2.2 Frontmatter YAML

Ogni pagina wiki **deve** avere un frontmatter YAML con almeno questi campi:

```yaml
---
title: "Titolo della Pagina"
type: source | entity | concept | topic | analysis | meta
created: 2026-07-18
updated: 2026-07-18
tags: [tag1, tag2, tag3]
sources: ["raw/articles/nome-fonte.md"]   # solo per pagine source
related: ["[[Pagina Collegata 1]]", "[[Pagina Collegata 2]]"]
confidence: high | medium | low           # quanto è solido il contenuto
---
```

**Campi aggiuntivi per tipo:**

- **source**: `source_type` (article, paper, note, transcript), `author`, `date_published`, `url`
- **entity**: `entity_type` (person, company, tool, place), `aliases`
- **concept**: `domain`, `complexity` (basic, intermediate, advanced)
- **analysis**: `query` (la domanda che l'ha generata), `scope`

### 2.3 Cross-reference

- Usare link Obsidian-style: `[[nome-pagina]]` per i riferimenti interni
- Usare link completi per riferimenti a fonti: `[titolo](../raw/articles/file.md)`
- Ogni pagina deve avere almeno un link in uscita (niente pagine orfane)

### 2.4 Citazioni

Quando una affermazione deriva da una fonte specifica, citarla inline:

```markdown
L'architettura transformer è stata introdotta nel 2017 [^1].

[^1]: Fonte: [[attention-is-all-you-need]] — Vaswani et al., 2017
```

---

## 3. Operazioni

### 3.1 INGEST — Ingestione di una nuova fonte

Trigger: l'utente aggiunge un file in `raw/` e chiede di processarlo.

**Workflow step-by-step:**

1. **Leggi** la fonte grezza per intero
2. **Discuti** i punti chiave con l'utente (3-5 takeaway principali)
3. **Crea** la scheda fonte in `wiki/sources/nome-fonte.md` con:
   - Frontmatter completo
   - Riassunto strutturato (300-500 parole)
   - Key takeaways (bullet list)
   - Citazioni rilevanti (quote dirette)
   - Link a pagine wiki esistenti che sono rilevanti
4. **Crea o aggiorna** pagine entity per ogni entità menzionata significativamente
5. **Crea o aggiorna** pagine concept per ogni concetto chiave
6. **Aggiorna** pagine topic rilevanti
7. **Controlla contradizioni**: se la nuova fonte contraddice conoscenza esistente, segnalalo in `wiki/meta/contradictions.md`
8. **Aggiorna `wiki/index.md`**: aggiungi le nuove pagine al catalogo
9. **Aggiorna `wiki/log.md`**: appendi un'entry con timestamp
10. **Aggiorna `wiki/overview.md`** se il quadro generale è cambiato significativamente

**Regola d'oro**: una singola ingestione può toccare 10-15 pagine. Non lesinare sugli aggiornamenti.

### 3.2 QUERY — Rispondere a domande

Trigger: l'utente fa una domanda sulla knowledge base.

**Workflow:**

1. **Leggi `wiki/index.md`** per identificare pagine rilevanti
2. **Leggi** le pagine wiki rilevanti (non le fonti grezze, a meno che serva verificare)
3. **Sintetizza** una risposta con citazioni alle pagine wiki
4. **Se la risposta è sostanziosa**: proponi di salvarla come pagina in `wiki/analyses/`
5. **Se emergono gap**: segnala cosa manca e suggerisci fonti da cercare

### 3.3 LINT — Manutenzione della wiki

Trigger: l'utente chiede un health-check, oppure ogni ~10 ingestioni.

**Checklist:**

- [ ] Pagine orfane (nessun link in ingresso)?
- [ ] Contradizioni non segnalate?
- [ ] Affermazioni obsolete (superate da fonti più recenti)?
- [ ] Concetti menzionati ma senza pagina dedicata?
- [ ] Cross-reference mancanti?
- [ ] Pagine troppo lunghe da splittare?
- [ ] Gap nella conoscenza? Suggerisci fonti da cercare.
- [ ] Tag inconsistenti o mancanti?

Output: aggiorna `wiki/meta/lint-report.md` con i findings.

### 3.4 EVOLVE — Aggiornare lo schema

Trigger: l'utente e l'LLM identificano un pattern migliore.

**Workflow:**

1. Discuti il cambiamento proposto
2. Aggiorna questo file (`CLAUDE.md`)
3. Se necessario, migra le pagine esistenti al nuovo formato
4. Logga il cambiamento in `wiki/log.md`

---

## 4. Formato del Log

Ogni entry in `wiki/log.md` segue questo formato per essere parsabile:

```markdown
## [YYYY-MM-DD HH:MM] tipo | Titolo

Descrizione breve dell'operazione.

- Pagine create: `[[pagina1]]`, `[[pagina2]]`
- Pagine aggiornate: `[[pagina3]]`
- Fonti processate: `raw/articles/file.md`
```

Tipi validi: `ingest`, `query`, `lint`, `evolve`, `fix`

---

## 5. Formato dell'Index

`wiki/index.md` è organizzato per categoria:

```markdown
# Wiki Index

## Sources (N)
| Pagina | Tipo | Data | Riassunto |
|--------|------|------|-----------|
| [[nome]] | article | 2026-07-18 | Breve descrizione |

## Entities (N)
...

## Concepts (N)
...

## Topics (N)
...

## Analyses (N)
...
```

---

## 6. Principi guida

1. **La wiki è il prodotto, non la chat.** Ogni insight va catturato nella wiki, non perso nella cronologia.
2. **Incrementale, non da zero.** Ogni ingestione costruisce su ciò che c'è già.
3. **Le contradizioni sono preziose.** Non nasconderle, segnalale esplicitamente.
4. **Link generosamente.** Più cross-reference = più valore composto.
5. **L'utente esplora, l'LLM mantiene.** L'utente non scrive la wiki: la legge, la naviga, la dirige.
6. **Lo schema evolve.** Questo file non è sacro — va aggiornato quando serve.
7. **Citare sempre.** Ogni affermazione deve essere tracciabile alla sua fonte.

---

## 7. Sessione di lavoro

All'inizio di ogni sessione:

1. Leggi `CLAUDE.md` (questo file)
2. Leggi `wiki/index.md` per orientarti
3. Leggi `wiki/log.md` (ultime 5-10 entry) per capire cosa è successo di recente
4. Chiedi all'utente cosa vuole fare: ingest, query, lint, o altro

---

## 8. Dominio corrente

**Nome wiki**: VisAi
**Focus**: Knowledge base personale di Andrea Masiero
**Lingua principale**: Italiano (con fonti anche in inglese)
**Strumenti**: Obsidian come viewer, LLM come writer
**Data di creazione**: 2026-07-18
