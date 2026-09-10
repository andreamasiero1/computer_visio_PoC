from src.core.interfaces import Listener
import time

class CountService(Listener):
    """
    Servizio di conteggio persone basato su line crossing.
    Implementa l'interfaccia Listener per ricevere eventi dal PersonService.
    
    Logica: definisci una linea virtuale (orizzontale o verticale).
    Per ogni persona tracciata, il servizio tiene in memoria la posizione precedente
    del centro del bounding box. Quando il centro attraversa la linea:
      - In una direzione → conta come INGRESSO (IN)
      - Nella direzione opposta → conta come USCITA (OUT)
    """
    
    def __init__(self):
        self.count_in = 0
        self.count_out = 0
        
        # Linee di conteggio.
        # Ogni linea è un dict: 
        #   {"name": "ingresso", "orientation": "horizontal", "position": 400, "in_direction": "down"}
        #
        # orientation: "horizontal" → la linea è orizzontale (si confronta la coordinata Y)
        #              "vertical"   → la linea è verticale (si confronta la coordinata X)
        # position:    il valore in pixel della linea (es. y=400 per una linea orizzontale)
        # in_direction: la direzione che conta come INGRESSO
        #               Per horizontal: "down" (dall'alto al basso) o "up" (dal basso all'alto)
        #               Per vertical:   "right" (da sinistra a destra) o "left" (da destra a sinistra)
        self._counting_lines: list[dict] = []
        
        # Posizione precedente del centro di ogni persona: { person_id: (center_x, center_y) }
        self._prev_positions: dict[int, tuple[int, int]] = {}
        
        # Storico eventi
        self._events_log: list[dict] = []
        
        print("✅ CountService: Inizializzato.")
    
    def set_counting_lines(self, lines: list[dict]) -> None:
        """
        Imposta le linee virtuali per il conteggio.
        
        Args:
            lines: Lista di linee. Ogni linea è un dict:
                   {"name": "ingresso", "orientation": "horizontal", "position": 400, "in_direction": "down"}
        """
        self._counting_lines = lines
        print(f"CountService: Impostate {len(lines)} linee di conteggio.")
        for line in lines:
            print(f"  → Linea '{line['name']}': {line['orientation']} a {line['position']}px, "
                  f"IN = {line['in_direction']}")
    
    def update(self, event_data: dict) -> None:
        """
        Riceve un evento dal PersonService.
        Controlla se il centro della persona ha attraversato una linea di conteggio.
        """
        if not self._counting_lines:
            return
        
        person_id = event_data.get("person_id")
        position = event_data.get("position")
        if person_id is None or position is None:
            return
        
        # Calcola il centro del bounding box
        center_x = (position["x1"] + position["x2"]) // 2
        center_y = (position["y1"] + position["y2"]) // 2
        
        # Se abbiamo una posizione precedente, verifica gli attraversamenti
        if person_id in self._prev_positions:
            prev_x, prev_y = self._prev_positions[person_id]
            
            for line in self._counting_lines:
                crossed, direction = self._check_crossing(
                    prev_x, prev_y, center_x, center_y, line
                )
                
                if crossed:
                    if direction == "in":
                        self.count_in += 1
                        event = {
                            "type": "IN",
                            "person_id": person_id,
                            "line": line["name"],
                            "timestamp": time.time()
                        }
                        self._events_log.append(event)
                        print(f"🟢 Persona {person_id} ENTRATA attraverso '{line['name']}' "
                              f"[IN: {self.count_in} | OUT: {self.count_out}]")
                    else:
                        self.count_out += 1
                        event = {
                            "type": "OUT",
                            "person_id": person_id,
                            "line": line["name"],
                            "timestamp": time.time()
                        }
                        self._events_log.append(event)
                        print(f"🔴 Persona {person_id} USCITA attraverso '{line['name']}' "
                              f"[IN: {self.count_in} | OUT: {self.count_out}]")
        
        # Aggiorna la posizione per il prossimo frame
        self._prev_positions[person_id] = (center_x, center_y)
    
    def _check_crossing(self, prev_x, prev_y, curr_x, curr_y, line: dict) -> tuple[bool, str]:
        """
        Controlla se il movimento da (prev) a (curr) ha attraversato la linea.
        
        Returns:
            (crossed: bool, direction: "in" | "out" | None)
        """
        orientation = line["orientation"]
        pos = line["position"]
        in_dir = line["in_direction"]
        
        if orientation == "horizontal":
            # La linea è orizzontale: confrontiamo la coordinata Y
            if prev_y <= pos < curr_y:
                # Attraversamento dall'alto verso il basso
                return True, "in" if in_dir == "down" else "out"
            elif prev_y >= pos > curr_y:
                # Attraversamento dal basso verso l'alto
                return True, "in" if in_dir == "up" else "out"
        
        elif orientation == "vertical":
            # La linea è verticale: confrontiamo la coordinata X
            if prev_x <= pos < curr_x:
                # Attraversamento da sinistra verso destra
                return True, "in" if in_dir == "right" else "out"
            elif prev_x >= pos > curr_x:
                # Attraversamento da destra verso sinistra
                return True, "in" if in_dir == "left" else "out"
        
        return False, None
    
    def get_counts(self) -> dict:
        """Restituisce i contatori attuali."""
        return {
            "in": self.count_in,
            "out": self.count_out,
            "currently_inside": self.count_in - self.count_out
        }
    
    def get_events_log(self) -> list[dict]:
        """Restituisce lo storico degli eventi di attraversamento."""
        return self._events_log
    
    def cleanup_lost_persons(self, active_person_ids: set) -> None:
        """
        Rimuove dalla memoria le persone che YOLO non traccia più.
        Evita che la memoria cresca all'infinito.
        """
        lost = [pid for pid in self._prev_positions if pid not in active_person_ids]
        for pid in lost:
            del self._prev_positions[pid]

