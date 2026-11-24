# job.py  ← déjà complet, ne pas modifier
 
from dataclasses import dataclass
from datetime import datetime
 
@dataclass
class Job:
    id: int
    format_entree: str
    format_sortie: str
    contenu: str
    soumis_le: datetime = None
 
    def __post_init__(self):
        if self.soumis_le is None:
            self.soumis_le = datetime.now()