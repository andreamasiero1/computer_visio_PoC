from src.repositories.in_memory_counter_repository import InMemoryCounterRepository
from src.services.blur_service import BlurService
from src.services.death_zone_service import DeathZoneService
from src.services.person_service import PersonService
from src.services.count_service import CountService
from src.services.main_service import MainService
from src.presentation.report import Report
from src.presentation.death_zone_ui import DeathZoneUI

def main():
    print("Inizializzazione del sistema...")
    
    # 1. Setup del Layer Repository
    # Usa SqliteCounterRepository per salvare su DB reale.
    repository = InMemoryCounterRepository()
    
    # 2. Setup dei Servizi base
    blur_service = BlurService()
    death_zone_service = DeathZoneService()
    person_service = PersonService()
    
    # 3. Collegamento del Pattern Observer (Listener)
    count_service = CountService()
    person_service.addListener(count_service)
    
    # 4. Inizializzazione Orchestratore (Dependency Injection)
    main_service = MainService(
        repository=repository,
        blur_service=blur_service,
        death_zone_service=death_zone_service,
        person_service=person_service
    )
    
    # 5. Setup Presentation Layer
    report_ui = Report(main_service)
    death_zone_ui = DeathZoneUI(main_service)
    
    print("Setup completato.")
    
    # Esempio di flusso d'uso (mock):
    death_zone_ui.configure_zones()
    
    # (Simulazione)
    # repository.save_count({"id": 1, "timestamp": "2026-08-28T10:00:00Z"})
    report_ui.generate_report()
    
    # Qui andrebbe il tipico loop video (cv2.VideoCapture)
    # while True:
    #     ret, frame = cap.read()
    #     if not ret: break
    #     processed_frame = main_service.process_frame(frame)
    #     cv2.imshow('Video', processed_frame)
    #     ...

if __name__ == "__main__":
    main()
