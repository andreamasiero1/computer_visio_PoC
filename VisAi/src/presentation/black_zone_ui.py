class BlackZoneUI:
    def __init__(self, main_service):
        self.main_service = main_service

    def configure_zones(self):
        """
        Gestisce l'input utente per configurare le zone morte.
        Es. legge da un file JSON, oppure usa un'interfaccia OpenCV per 
        disegnare poligoni col mouse.
        Alla fine invia le zone al main_service.
        """
        # Esempio fittizio
        zones = [
            {"points": [(0, 0), (100, 0), (100, 100), (0, 100)]}
        ]
        print(f"DeathZoneUI: Impostazione di {len(zones)} zone morte.")
        self.main_service.setDeadZones(zones)
