# main.py
from job import Job
from file_attente import FileAttente
from workers import WorkerConsole
 
file = FileAttente()
 
file.soumettre(Job(1, "csv", "json", "nom,ville\nAlice,Montréal\n"))
file.soumettre(Job(2, "json", "csv", '[{"nom":"Bob","ville":"Québec"}]'))
file.soumettre(Job(3, "csv", "json", "a,b\n1,2\n"))
 
print(f"Jobs en attente : {file.nb_en_attente()}")
 
worker = WorkerConsole()
while file.nb_en_attente() > 0:
    file.traiter_prochain(worker)
 
print(f"Jobs en attente : {file.nb_en_attente()}")