# 🛠️ Piano di Lavoro — PoC Conteggio Capi Camerini

> **Progetto**: GuardIA (ex VisAi)  
> **Scope PoC**: Monitoraggio ingressi/uscite camerini con conteggio capi  
> **Data**: Luglio 2026  
> **Durata stimata**: 8–10 settimane

---

## 1. Obiettivo del PoC

Dimostrare la fattibilità tecnica di un sistema che:
1. Rileva e traccia le **persone** che entrano/escono da un camerino
2. Rileva i **capi di abbigliamento** che ogni persona porta con sé
3. **Conta** i capi in entrata (`IN`) e in uscita (`OUT`)
4. Genera un **alert** quando `Δ = IN - OUT > 0` (capi mancanti)

**Vincolo critico**: nessuna ripresa dell'interno del camerino — solo entrata e uscita.

---

## 2. Stack Tecnologico Completo

### 2.1 Linguaggio e Runtime

| Componente | Tecnologia | Versione | Motivazione |
|------------|------------|----------|-------------|
| **Linguaggio** | Python | 3.11+ | Ecosistema AI/ML più maturo, prototipazione rapida |
| **Package manager** | `uv` | latest | Più veloce di pip, gestione ambienti pulita |
| **Ambiente virtuale** | `venv` via uv | — | Isolamento dipendenze |

### 2.2 Deep Learning & Computer Vision

| Componente | Tecnologia | Motivazione |
|------------|------------|-------------|
| **Framework DL** | PyTorch 2.x | Standard de facto per la ricerca, supporto CUDA |
| **Person Detection** | YOLOv8 / YOLOv11 (Ultralytics) | Stato dell'arte in velocità/accuratezza, API semplice |
| **Object Detection (capi)** | YOLOv8 fine-tuned | Stesso framework, fine-tuning su dataset abbigliamento |
| **Multi-Object Tracking** | ByteTrack (integrato in Ultralytics) | Tracking robusto, zero-shot, già integrato |
| **Video I/O** | OpenCV (`cv2`) | Cattura video da webcam, file o stream RTSP |
| **Elaborazione immagini** | OpenCV + NumPy | Preprocessing, disegno ROI, linee virtuali |

### 2.3 Dataset per Fine-Tuning

| Dataset | Uso | Note |
|---------|-----|------|
| **DeepFashion2** | Training object detection capi | ~491K immagini, 801K istanze di abbigliamento, 13 categorie |
| **ModaNet** | Alternativa/integrazione | ~55K immagini street-fashion annotate |
| **Dataset custom** | Fine-tuning finale | Video registrati in ambiente controllato (simulazione camerino) |
| **COCO** | Pre-training person detection | YOLOv8 pre-trained su COCO include già classe "person" |

### 2.4 Backend & API

| Componente | Tecnologia | Motivazione |
|------------|------------|-------------|
| **API Server** | FastAPI | Async, veloce, auto-documentazione OpenAPI |
| **Database** | SQLite | Leggero, zero config, perfetto per PoC |
| **ORM** | SQLModel | Integrazione nativa con FastAPI + SQLite |
| **WebSocket** | FastAPI WebSocket | Streaming real-time degli alert alla dashboard |

### 2.5 Frontend / Dashboard

| Componente | Tecnologia | Motivazione |
|------------|------------|-------------|
| **Framework** | React + Vite | Build veloce, componenti riutilizzabili |
| **UI Library** | Shadcn/ui | Componenti pronti, design professionale |
| **Video stream** | HTML5 `<video>` + Canvas | Visualizzazione feed con overlay delle bounding box |
| **Real-time** | WebSocket | Ricezione alert in tempo reale |
| **Grafici** | Recharts | Statistiche e conteggi |

### 2.6 Infrastruttura & DevOps

| Componente | Tecnologia | Motivazione |
|------------|------------|-------------|
| **Containerizzazione** | Docker + Docker Compose | Ambiente riproducibile, deployment semplificato |
| **GPU** | CUDA 12.x + cuDNN | Accelerazione inferenza su GPU NVIDIA |
| **Logging** | Loguru | Logging strutturato Python, più ergonomico di logging stdlib |
| **Config** | Pydantic Settings | Configurazione tipizzata da env vars / file .env |
| **Version control** | Git | — |

### 2.7 Testing & Qualità

| Componente | Tecnologia | Motivazione |
|------------|------------|-------------|
| **Unit test** | pytest | Standard Python |
| **Linting** | Ruff | Linter+formatter velocissimo, all-in-one |
| **Type checking** | mypy (opzionale) | Validazione tipi statici |

---

## 3. Architettura del PoC

```
┌─────────────────────────────────────────────────────────────────┐
│                        VIDEO INPUT                              │
│         (webcam / file .mp4 / stream RTSP)                      │
└─────────────────┬───────────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    DETECTION ENGINE                             │
│                                                                 │
│  ┌──────────────────┐    ┌──────────────────────┐               │
│  │ YOLOv8 - Person  │    │ YOLOv8 - Clothing    │               │
│  │ Detection        │    │ Detection (fine-tuned)│               │
│  └────────┬─────────┘    └──────────┬───────────┘               │
│           │                         │                           │
│           ▼                         ▼                           │
│  ┌──────────────────┐    ┌──────────────────────┐               │
│  │ ByteTrack        │    │ Association Logic     │               │
│  │ (Person Tracking)│───▶│ (Person ↔ Clothing)  │               │
│  └────────┬─────────┘    └──────────┬───────────┘               │
│           │                         │                           │
└───────────┼─────────────────────────┼───────────────────────────┘
            │                         │
            ▼                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    COUNTING ENGINE                              │
│                                                                 │
│  ┌──────────────────────────────────────────────┐               │
│  │          VIRTUAL LINE (ROI)                   │               │
│  │                                               │               │
│  │  Person crosses IN  → count clothing items   │               │
│  │  Person crosses OUT → count clothing items   │               │
│  │                                               │               │
│  │  Δ = COUNT_IN - COUNT_OUT                    │               │
│  │  if Δ > 0 → ALERT                           │               │
│  └──────────────────────────────────────────────┘               │
│                                                                 │
└─────────────────┬───────────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    BACKEND (FastAPI)                             │
│                                                                 │
│  ┌────────────┐  ┌────────────┐  ┌──────────────┐              │
│  │ REST API   │  │ WebSocket  │  │ SQLite DB    │              │
│  │ /events    │  │ /ws/alerts │  │ events.db    │              │
│  └────────────┘  └────────────┘  └──────────────┘              │
│                                                                 │
└─────────────────┬───────────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FRONTEND (React)                              │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌────────────────┐          │
│  │ Live Video  │  │ Alert Panel │  │ Statistics     │          │
│  │ + Overlays  │  │ (real-time) │  │ (grafici)      │          │
│  └─────────────┘  └─────────────┘  └────────────────┘          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Struttura del Progetto

```
guardia-poc/
├── docker-compose.yml
├── .env
├── README.md
│
├── backend/
│   ├── Dockerfile
│   ├── pyproject.toml
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI entrypoint
│   │   ├── config.py               # Pydantic Settings
│   │   │
│   │   ├── detection/
│   │   │   ├── __init__.py
│   │   │   ├── person_detector.py  # YOLOv8 person detection
│   │   │   ├── clothing_detector.py # YOLOv8 clothing detection
│   │   │   ├── tracker.py          # ByteTrack wrapper
│   │   │   └── associator.py       # Person ↔ Clothing association
│   │   │
│   │   ├── counting/
│   │   │   ├── __init__.py
│   │   │   ├── line_counter.py     # Virtual line crossing logic
│   │   │   ├── session_manager.py  # Gestione sessione per persona
│   │   │   └── alert_engine.py     # Generazione alert
│   │   │
│   │   ├── video/
│   │   │   ├── __init__.py
│   │   │   ├── capture.py          # Video capture (webcam/RTSP/file)
│   │   │   ├── pipeline.py         # Orchestrazione pipeline completa
│   │   │   └── annotator.py        # Disegno overlay su frame
│   │   │
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # REST endpoints
│   │   │   └── websocket.py        # WebSocket per alert real-time
│   │   │
│   │   └── db/
│   │       ├── __init__.py
│   │       ├── models.py           # SQLModel schemas
│   │       └── database.py         # SQLite connection
│   │
│   ├── models/                     # Pesi dei modelli YOLOv8
│   │   ├── yolov8n.pt              # Person detection (pre-trained)
│   │   └── clothing_best.pt        # Clothing detection (fine-tuned)
│   │
│   ├── data/
│   │   ├── test_videos/            # Video di test
│   │   └── datasets/               # Dataset per fine-tuning
│   │
│   └── tests/
│       ├── test_detection.py
│       ├── test_counting.py
│       └── test_api.py
│
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── src/
│   │   ├── App.tsx
│   │   ├── components/
│   │   │   ├── VideoFeed.tsx       # Stream video con overlay
│   │   │   ├── AlertPanel.tsx      # Lista alert in tempo reale
│   │   │   ├── StatsCard.tsx       # Card con statistiche
│   │   │   └── SessionLog.tsx      # Log sessioni camerino
│   │   ├── hooks/
│   │   │   └── useWebSocket.ts     # Hook per connessione WS
│   │   └── lib/
│   │       └── api.ts              # Client API
│   └── ...
│
├── scripts/
│   ├── download_models.sh          # Scarica pesi pre-trained
│   ├── prepare_dataset.py          # Prepara dataset per fine-tuning
│   └── train_clothing.py           # Script fine-tuning YOLOv8
│
└── notebooks/
    ├── 01_person_detection.ipynb    # Esperimenti person detection
    ├── 02_clothing_detection.ipynb  # Esperimenti clothing detection
    ├── 03_tracking_test.ipynb       # Test tracking + line crossing
    └── 04_end_to_end.ipynb          # Pipeline completa
```

---

## 5. Piano di Lavoro Fase per Fase

---

### FASE 1 — Setup & Ambiente (Settimana 1)

**Obiettivo**: ambiente di sviluppo funzionante con video input e prima detection.

| # | Task | Output atteso |
|---|------|---------------|
| 1.1 | Creare la struttura del progetto (`guardia-poc/`) | Directory tree completo |
| 1.2 | Configurare `pyproject.toml` con dipendenze | Ambiente Python riproducibile |
| 1.3 | Setup Docker + `docker-compose.yml` | Container backend + frontend |
| 1.4 | Installare PyTorch + CUDA + Ultralytics | `import torch; torch.cuda.is_available()` → True |
| 1.5 | Implementare `video/capture.py` | Cattura da webcam, file .mp4 o RTSP |
| 1.6 | Test: visualizzare un video con OpenCV | Finestra con video in riproduzione |

**Dipendenze da installare**:
```
torch>=2.3
torchvision>=0.18
ultralytics>=8.2
opencv-python>=4.9
numpy>=1.26
fastapi>=0.111
uvicorn>=0.30
sqlmodel>=0.0.19
websockets>=12.0
pydantic-settings>=2.3
loguru>=0.7
```

**Deliverable**: video input funzionante da tutte e 3 le sorgenti (webcam, file, RTSP).

---

### FASE 2 — Person Detection + Tracking (Settimane 2–3)

**Obiettivo**: rilevare e tracciare le persone attraverso i frame, con ID persistente.

| # | Task | Output atteso |
|---|------|---------------|
| 2.1 | Integrare YOLOv8n per person detection | Bounding box su ogni persona nel frame |
| 2.2 | Filtrare solo la classe `person` (class_id=0 in COCO) | Nessun altro oggetto rilevato |
| 2.3 | Integrare ByteTrack per multi-object tracking | Ogni persona ha un ID persistente tra frame |
| 2.4 | Definire la **ROI** (Region of Interest) del camerino | Area rettangolare configurabile |
| 2.5 | Definire la **virtual line** all'ingresso del camerino | Linea che separa "fuori" da "dentro" |
| 2.6 | Implementare **line-crossing detection** | Evento "PERSON_IN" / "PERSON_OUT" generato |
| 2.7 | Notebook `01_person_detection.ipynb` | Documentazione esperimenti |

**Logica line-crossing**:
```python
# Per ogni persona tracciata:
# 1. Calcola il centroid del bounding box
# 2. Confronta la posizione del centroid rispetto alla linea virtuale
# 3. Se il centroid passa da "sopra" a "sotto" la linea → IN
# 4. Se il centroid passa da "sotto" a "sopra" la linea → OUT
```

**Deliverable**: video annotato con bounding box + ID persona + eventi IN/OUT stampati in console.

---

### FASE 3 — Clothing Detection (Settimane 4–5)

**Obiettivo**: rilevare i capi di abbigliamento trasportati da ogni persona.

| # | Task | Output atteso |
|---|------|---------------|
| 3.1 | Scaricare e preparare il dataset **DeepFashion2** | Dataset formattato in YOLO format |
| 3.2 | Selezionare le categorie rilevanti (maglie, pantaloni, giacche, vestiti, gonne) | Dataset filtrato |
| 3.3 | Scrivere `scripts/prepare_dataset.py` | Conversione annotation → YOLO format |
| 3.4 | Fine-tuning YOLOv8n su clothing detection | Modello `clothing_best.pt` |
| 3.5 | Valutare mAP su validation set | mAP@0.5 ≥ 0.70 (target PoC) |
| 3.6 | Implementare `clothing_detector.py` | Bounding box su capi in mano/braccio |
| 3.7 | Notebook `02_clothing_detection.ipynb` | Documentazione training + metriche |

**Comandi fine-tuning**:
```bash
yolo detect train \
    model=yolov8n.pt \
    data=clothing_dataset.yaml \
    epochs=100 \
    imgsz=640 \
    batch=16 \
    name=clothing_detector
```

**Sfida principale**: rilevare capi **in mano** o **sul braccio** (non indossati). Potrebbe servire un dataset custom supplementare.

**Deliverable**: modello che rileva capi di abbigliamento con mAP ≥ 0.70.

---

### FASE 4 — Association Person↔Clothing (Settimana 6)

**Obiettivo**: associare i capi rilevati alla persona che li trasporta.

| # | Task | Output atteso |
|---|------|---------------|
| 4.1 | Implementare `associator.py` | Ogni capo è associato a un person_id |
| 4.2 | Logica di associazione basata su IoU/distanza | Capo assegnato alla persona più vicina |
| 4.3 | Gestire casi edge (capi tra due persone, capi a terra) | Regole di fallback |
| 4.4 | Implementare `session_manager.py` | Sessione per persona: {person_id, items_in, items_out, status} |
| 4.5 | Notebook `03_tracking_test.ipynb` | Test integrato detection + tracking + association |

**Logica di associazione**:
```python
def associate_clothing_to_person(persons, clothing_items):
    """
    Per ogni capo rilevato:
    1. Calcola l'overlap (IoU) con ogni bounding box persona
    2. Se IoU > soglia → associa al persona
    3. Se nessun overlap → calcola distanza centroid-centroid
    4. Associa alla persona più vicina entro un raggio massimo
    """
```

**Deliverable**: visualizzazione con persona + capi associati colorati per persona.

---

### FASE 5 — Counting Engine + Alert (Settimana 7)

**Obiettivo**: contare i capi IN/OUT e generare alert.

| # | Task | Output atteso |
|---|------|---------------|
| 5.1 | Implementare `line_counter.py` | Conteggio capi quando persona attraversa la linea |
| 5.2 | Evento `ENTER`: salva `count_in = N capi rilevati` | Log evento con conteggio |
| 5.3 | Evento `EXIT`: salva `count_out = N capi rilevati` | Log evento con conteggio |
| 5.4 | Calcolo `Δ = count_in - count_out` | Valore Δ calcolato per sessione |
| 5.5 | Implementare `alert_engine.py` | Alert generato se Δ > 0 |
| 5.6 | Salvare eventi su SQLite | Tabella `events` con tutti i dati |
| 5.7 | Notebook `04_end_to_end.ipynb` | Test pipeline completa |

**Schema database (SQLite)**:
```sql
CREATE TABLE fitting_room_sessions (
    id            INTEGER PRIMARY KEY,
    person_id     INTEGER NOT NULL,
    entered_at    TIMESTAMP NOT NULL,
    exited_at     TIMESTAMP,
    items_in      INTEGER DEFAULT 0,
    items_out     INTEGER DEFAULT 0,
    delta         INTEGER DEFAULT 0,
    alert         BOOLEAN DEFAULT FALSE,
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE alerts (
    id            INTEGER PRIMARY KEY,
    session_id    INTEGER REFERENCES fitting_room_sessions(id),
    delta         INTEGER NOT NULL,
    frame_path    TEXT,           -- screenshot del momento dell'alert
    acknowledged  BOOLEAN DEFAULT FALSE,
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Deliverable**: pipeline end-to-end che conta capi e genera alert in console/log.

---

### FASE 6 — Backend API (Settimana 8)

**Obiettivo**: esporre i dati tramite REST API e WebSocket.

| # | Task | Output atteso |
|---|------|---------------|
| 6.1 | Implementare `main.py` (FastAPI) | Server avviabile con `uvicorn` |
| 6.2 | Endpoint `GET /api/sessions` | Lista sessioni camerino |
| 6.3 | Endpoint `GET /api/alerts` | Lista alert attivi |
| 6.4 | Endpoint `GET /api/stats` | Statistiche aggregate (totale in/out, alert rate) |
| 6.5 | WebSocket `/ws/alerts` | Push alert in tempo reale |
| 6.6 | WebSocket `/ws/video` | Stream video annotato (MJPEG) |
| 6.7 | Scrivere test API con pytest | Tutti i test passano |

**Deliverable**: API funzionante documentata su `http://localhost:8000/docs`.

---

### FASE 7 — Frontend Dashboard (Settimane 9–10)

**Obiettivo**: dashboard web per visualizzare il sistema in azione.

| # | Task | Output atteso |
|---|------|---------------|
| 7.1 | Setup progetto React + Vite | App avviabile |
| 7.2 | Componente `VideoFeed` | Stream video live con overlay (bounding box, linea virtuale, conteggi) |
| 7.3 | Componente `AlertPanel` | Lista alert in tempo reale con colori (rosso = attivo, verde = risolto) |
| 7.4 | Componente `StatsCard` | Card con KPI: totale sessioni, totale alert, tasso di alert |
| 7.5 | Componente `SessionLog` | Tabella cronologica delle sessioni camerino |
| 7.6 | Connessione WebSocket | Alert push in tempo reale |
| 7.7 | Docker setup frontend | Container con Nginx per servire il build |
| 7.8 | Test end-to-end completo | Demo funzionante |

**Deliverable**: dashboard accessibile su `http://localhost:3000` con video live + alert.

---

## 6. Timeline Riassuntiva

```
Settimana  1  ████░░░░░░░░░░░░░░░░  Setup & Ambiente
Settimana  2  ░░░░████░░░░░░░░░░░░  Person Detection
Settimana  3  ░░░░░░░░████░░░░░░░░  Person Tracking + Line Crossing
Settimana  4  ░░░░░░░░░░░░████░░░░  Clothing Detection (dataset)
Settimana  5  ░░░░░░░░░░░░░░░░████  Clothing Detection (training)
Settimana  6  ░░░░░░░░░░░░░░░░░░░░████  Association Logic
Settimana  7  ░░░░░░░░░░░░░░░░░░░░░░░░████  Counting + Alert
Settimana  8  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░████  Backend API
Settimana  9  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████  Frontend
Settimana 10  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████  Test & Demo
```

---

## 7. Hardware Minimo per Sviluppo PoC

| Componente | Minimo | Consigliato |
|------------|--------|-------------|
| **GPU** | NVIDIA GTX 1660 (6GB VRAM) | NVIDIA RTX 3060+ (12GB VRAM) |
| **CPU** | Intel i5 / Apple M1 | Intel i7 / Apple M2 Pro+ |
| **RAM** | 16 GB | 32 GB |
| **Storage** | 50 GB liberi (modelli + dataset) | 100 GB+ SSD |
| **Webcam** | Qualsiasi USB (per test) | Logitech C920+ (1080p) |

> **Nota**: per lo sviluppo su Mac con Apple Silicon (M1/M2/M3), PyTorch supporta il backend `mps` (Metal Performance Shaders) come alternativa a CUDA. Le performance sono inferiori rispetto a GPU NVIDIA dedicate ma sufficienti per un PoC.

---

## 8. Rischi e Mitigazioni del PoC

| Rischio | Probabilità | Mitigazione |
|---------|-------------|-------------|
| **Clothing detection scarsa** (capi in mano poco rilevati) | Alta | Registrare video custom per fine-tuning supplementare |
| **Tracking ID swap** (persona perde l'ID) | Media | Usare Re-ID features + soglia di distanza conservativa |
| **Conteggio errato** (capi sovrapposti/occlusi) | Alta | Accettare margine di errore nel PoC; migliorare con dati reali |
| **Performance insufficiente** (FPS troppo bassi) | Media | Usare YOLOv8n (nano); ridurre risoluzione input; batch processing |
| **Falsi alert** (persona esce con capo indossato) | Alta | Per il PoC, documentare come limitazione nota; risolvibile con Re-ID avanzata |

---

## 9. Criteri di Successo del PoC

| KPI | Target PoC | Note |
|-----|-----------|------|
| Person detection accuracy | ≥ 95% | Su video di test controllati |
| Clothing detection mAP@0.5 | ≥ 70% | Su validation set DeepFashion2 |
| Conteggio corretto IN/OUT | ≥ 80% | Su scenario semplice (1 persona, 1-5 capi) |
| Alert corretto (Δ > 0) | ≥ 75% | Su scenario semplice |
| FPS pipeline completa | ≥ 10 FPS | Su GPU target |
| Latenza alert | < 3 secondi | Da evento a visualizzazione dashboard |

---

## 10. Comandi Rapidi per Iniziare

```bash
# 1. Crea la struttura del progetto
mkdir -p guardia-poc/{backend/{app/{detection,counting,video,api,db},models,data/{test_videos,datasets},tests},frontend/src/{components,hooks,lib},scripts,notebooks}

# 2. Inizializza il backend
cd guardia-poc/backend
uv init
uv add torch torchvision ultralytics opencv-python numpy fastapi uvicorn sqlmodel websockets pydantic-settings loguru

# 3. Verifica GPU
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}, MPS: {torch.backends.mps.is_available()}')"

# 4. Test rapido YOLOv8
python -c "from ultralytics import YOLO; model = YOLO('yolov8n.pt'); results = model.predict(source=0, show=True)"

# 5. Inizializza il frontend
cd ../frontend
npx -y create-vite@latest ./ --template react-ts
npm install
```

---

*Piano di lavoro v1.0 — Luglio 2026*
