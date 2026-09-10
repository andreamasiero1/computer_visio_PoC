# Computer Vision PoC - VisAi

Questo è uno scheletro applicativo generato sulla base di un'architettura UML a 3 layer (Presentation, Services, Repository).

## Struttura
- `src/core/`: Interfacce base (es. `Listener`, `ICounterRepository`).
- `src/repositories/`: Logica per il salvataggio dei dati (SQLite o In-Memory).
- `src/services/`: Logica di business (es. tracciamento persone, oscuramento zone, filtri privacy).
- `src/presentation/`: Strati superficiali (UI, report).

## Come eseguire

Assicurati di avere le dipendenze base:
```bash
pip install -r requirements.txt
```

Per avviare la simulazione e testare l'architettura:
```bash
# Da questa cartella VisAi/ eseguire:
export PYTHONPATH=$(pwd)
python3 src/main.py
```
