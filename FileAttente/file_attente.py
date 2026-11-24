# file_attente.py  ← À COMPLÉTER
 
import threading
from job import Job
from workers import Worker
 
class FileAttente:
    _instance = None
    _verrou_classe = threading.Lock()
 
    def __new__(cls):
        # TODO : implémenter le Singleton
        pass
 
    def _initialiser(self):
        # TODO : initialiser la liste de jobs
        pass
 
    def soumettre(self, job: Job) -> None:
        # TODO : ajouter le job à la file
        pass
 
    def traiter_prochain(self, worker: Worker) -> str | None:
        # TODO : retirer le premier job et le faire traiter par le worker
        # Retourner None si la file est vide
        pass
 
    def nb_en_attente(self) -> int:
        # TODO : retourner le nombre de jobs dans la file
        pass