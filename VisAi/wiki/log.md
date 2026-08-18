---
title: "Wiki Log"
type: meta
created: 2026-07-18
updated: 2026-08-19
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

---

## [2026-07-18 10:52] ingest | PyTorch in One Hour

Seconda ingestione della wiki. Processato il tutorial completo su PyTorch di Sebastian Raschka (2025).

- **Fonte processata**: `raw/PyTorch in One Hour From Tensors to Training Neural Networks on Multiple GPUs.md`
- **Pagine create**:
  - `wiki/sources/pytorch-in-one-hour.md` — Scheda fonte del tutorial
  - `wiki/entities/sebastian-raschka.md` — Pagina entità: Sebastian Raschka (autore)
  - `wiki/entities/pytorch.md` — Pagina entità: PyTorch (framework)
  - `wiki/concepts/tensor.md` — Pagina concetto: Tensor
  - `wiki/concepts/autograd.md` — Pagina concetto: Autograd (differenziazione automatica)
  - `wiki/concepts/distributed-data-parallel.md` — Pagina concetto: DDP (training multi-GPU)
- **Pagine aggiornate**: `wiki/index.md`, `wiki/overview.md`, `wiki/topics/deep-learning-nlp.md`, `wiki/concepts/transformer.md`
- **Key takeaway**: PyTorch ha 3 componenti core (tensor library, autograd, deep learning utilities). Il training loop standard è forward→loss→zero_grad→backward→step. DDP permette training multi-GPU con scalabilità quasi lineare.
- **Nessuna contraddizione** rilevata con la knowledge base esistente

---

## [2026-07-18 11:10] ingest | README Progetto VisAi

Terza ingestione della wiki. Processato il documento fondativo del progetto VisAi — anti-theft AI per retail.

- **Fonte processata**: `README.md` (root del progetto)
- **Nuovo dominio**: Computer Vision per la Sicurezza Retail
- **Pagine create**:
  - `wiki/sources/visai-progetto-readme.md` — Scheda fonte del README
  - `wiki/concepts/edge-ai.md` — Pagina concetto: Edge AI (architettura processing locale)
  - `wiki/concepts/action-recognition.md` — Pagina concetto: Action Recognition / Pose Estimation
  - `wiki/concepts/object-counting.md` — Pagina concetto: Object Counting / Re-Identification
  - `wiki/topics/computer-vision-retail-security.md` — Nuovo topic: CV per sicurezza retail
- **Pagine aggiornate**: `wiki/index.md`, `wiki/overview.md`
- **Key takeaway**: VisAi mira a sostituire i sistemi antitaccheggio fisici con computer vision ed Edge AI. Due core feature: anomaly detection comportamentale e conteggio capi camerini. Architettura edge-first con hardware proprietario.
- **Nessuna contraddizione** rilevata — questo è un dominio completamente nuovo rispetto alle fonti precedenti

---

## [2026-07-27 12:00] ingest | Analisi Business & Strategia di Mercato

Quarta ingestione della wiki. Processata l'analisi di mercato, modelli di ricavo, pricing e benchmarking competitivo.

- **Pagine create**:
  - `wiki/concepts/retail-shrinkage.md` — Differenze inventariali e benchmark OVS/Mango
  - `wiki/concepts/revenue-models-visai.md` — Modelli di ricavo SaaS e Pay-per-Prevention
  - `wiki/concepts/product-strategy-lean-vs-full.md` — Strategia Lean (cam esistenti) vs Full Revolution
  - `wiki/concepts/competitor-analysis-loss-prevention.md` — Benchmark competitor (Veesion, Amazon JWO, Standard AI)
- **Pagine aggiornate**: `wiki/index.md`, `wiki/overview.md`, `wiki/topics/computer-vision-retail-security.md`
- **Key takeaway**: Decisione strategica per approccio Lean iniziale con telecamere esistenti ed evoluzione successiva verso hardware custom; validazione mercato retail fast fashion.

---

## [2026-08-19 01:45] ingest | Architettura e Logica del Flusso Sequenziale

Quinta ingestione della wiki. Processato il documento di riferimento per la pipeline di elaborazione video, riconoscimento azioni e innesco allarmi del sistema VisAi.

- **Fonte processata**: `VisAi/raw/notes/architettura-flusso-sequenziale.md`
- **Pagine create**:
  - `wiki/sources/architettura-flusso-sequenziale.md` — Scheda fonte dell'architettura sequenziale
  - `wiki/concepts/cascade-funnel-pipeline.md` — Pagina concetto: Architettura a imbuto (Cascade Funnel)
  - `wiki/concepts/capo-vivo.md` — Pagina concetto: Capo Vivo e tracciamento selettivo
  - `wiki/concepts/logica-booleana-allarme.md` — Pagina concetto: Logica booleana e validazione temporale 10s
- **Pagine aggiornate**:
  - `wiki/concepts/action-recognition.md` — Integrato trigger esclusivo su Capo Vivo (Fase 4)
  - `wiki/concepts/edge-ai.md` — Integrati benefici del Cascade Funnel per ottimizzazione Edge
  - `wiki/topics/computer-vision-retail-security.md` — Integrata pipeline sequenziale a 5 fasi
  - `wiki/index.md` — Aggiornato indice generale (27 pagine totali)
  - `wiki/overview.md` — Aggiornata panoramica, metriche e grafo connessioni
- **Key takeaway**:
  - **Cascade Funnel**: L'Action Recognition pesante gira solo sull'intersezione Persona-Capo Vivo, risparmiando il 95%+ di calcolo Edge.
  - **Zone Morte & Filtri**: Mascheramento statico via GUI e filtro valore (€40-50+) eliminano rumore ed evitano overhead da scene understanding.
  - **Doppia Verifica 10s**: Timer di validazione per eliminare i falsi positivi dovuti a rotazioni del corpo o occlusioni temporanee.
- **Nessuna contraddizione** rilevata con le fonti precedenti.
