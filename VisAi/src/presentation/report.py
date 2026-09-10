class Report:
    def __init__(self, main_service):
        self.main_service = main_service

    def generate_report(self):
        """
        Recupera i dati dal MainService e li presenta
        (es. stampa in console, salva come CSV, o invia via API JSON).
        """
        stats = self.main_service.getStats()
        print("=== REPORT STATISTICHE ===")
        for s in stats:
            print(s)
        print("==========================")
