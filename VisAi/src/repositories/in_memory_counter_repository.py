from src.core.interfaces import ICounterRepository

class InMemoryCounterRepository(ICounterRepository):
    def __init__(self):
        self._counts = []

    def save_count(self, count_data: dict) -> None:
        """Salva un conteggio in memoria."""
        self._counts.append(count_data)

    def get_counts(self) -> list:
        """Restituisce la lista in memoria dei conteggi."""
        return self._counts
