---
title: "Wiki Log"
type: meta
created: 2026-07-18
updated: 2026-07-18
---

# 📋 Log — VisAi

> Registro cronologico di tutte le operazioni sulla wiki.
> Formato parsabile: `grep "^## \[" wiki/log.md | tail -5`

---

## [2026-07-18 00:55] evolve | Inizializzazione Wiki

Creazione della struttura iniziale della wiki VisAi.

- **Operazione**: Setup completo del sistema LLM Wiki
- **File creati**:
  - `CLAUDE.md` — Schema operativo con regole, convenzioni e workflow
  - `wiki/index.md` — Catalogo pagine (vuoto, pronto per l'uso)
  - `wiki/log.md` — Questo file di log
  - `wiki/overview.md` — Panoramica generale
- **Struttura directory**:
  - `raw/articles/` — Per articoli web
  - `raw/papers/` — Per paper accademici
  - `raw/notes/` — Per appunti personali
  - `raw/transcripts/` — Per trascrizioni
  - `raw/assets/` — Per immagini e allegati
  - `wiki/sources/` — Schede riassuntive delle fonti
  - `wiki/entities/` — Pagine entità
  - `wiki/concepts/` — Pagine concetto
  - `wiki/topics/` — Pagine topic
  - `wiki/analyses/` — Analisi e sintesi
  - `wiki/meta/` — Pagine meta e manutenzione
- **Stato**: Wiki pronta per la prima ingestione

---

## [2026-07-18 00:58] ingest | Attention Is All You Need

Prima ingestione della wiki. Processato il paper fondativo del Transformer (Vaswani et al., 2017).

- **Fonte processata**: `raw/papers/attention-is-all-you-need.md`
- **Pagine create**:
  - `wiki/sources/attention-is-all-you-need.md` — Scheda fonte del paper
  - `wiki/concepts/transformer.md` — Pagina concetto: architettura Transformer
  - `wiki/concepts/self-attention.md` — Pagina concetto: meccanismo di Self-Attention
  - `wiki/topics/deep-learning-nlp.md` — Pagina topic: Deep Learning & NLP
- **Pagine aggiornate**: `wiki/index.md`, `wiki/overview.md`
- **Key takeaway**: il Transformer elimina ricorrenza e convoluzioni, basandosi solo su self-attention. Ha rivoluzionato il campo ed è il fondamento di tutti gli LLM moderni.
- **Pagine da creare in futuro**: entità per gli autori, concetti per multi-head-attention e positional-encoding
