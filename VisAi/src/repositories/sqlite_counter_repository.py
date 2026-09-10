from src.core.interfaces import ICounterRepository

class SqliteCounterRepository(ICounterRepository):
    def __init__(self, db_path: str = "counter.db"):
        self.db_path = db_path
        # TODO: Implementare connessione al DB SQLite
        
    def save_count(self, count_data: dict) -> None:
        """Salva un conteggio su DB SQLite."""
        # TODO: Implementare query INSERT
        pass

    def get_counts(self) -> list:
        """Restituisce la cronologia dal DB SQLite."""
        # TODO: Implementare query SELECT
        return []
