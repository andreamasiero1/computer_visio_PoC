from abc import ABC, abstractmethod

class Listener(ABC):
    @abstractmethod
    def update(self, event_data: dict) -> None:
        """Metodo chiamato quando il listener riceve una notifica."""
        pass

class ICounterRepository(ABC):
    @abstractmethod
    def save_count(self, count_data: dict) -> None:
        """Salva i dati di conteggio."""
        pass

    @abstractmethod
    def get_counts(self) -> list:
        """Recupera lo storico dei conteggi."""
        pass
