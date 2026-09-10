from src.core.interfaces import Listener

class CountService(Listener):
    def __init__(self):
        self.current_count = 0

    def update(self, event_data: dict) -> None:
        """
        Riceve l'evento di notifica (es. da PersonService).
        Aggiorna il contatore interno.
        """
        # TODO: logica di incremento contatore basata su event_data
        print(f"CountService: Ricevuto evento -> {event_data}")
        self.current_count += 1
