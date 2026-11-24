# main.py

from journal import Journal

# Module de conversion
def convertir_fichier(nom: str) -> None:
    journal1 = Journal()
    journal1.enregistrer(f"Début de la conversion : {nom}")
    # ... conversion ...
    journal1.enregistrer(f"Conversion réussie : {nom}")

# Module de validation
def valider_fichier(nom: str) -> bool:
    journal2 = Journal()
    journal2.enregistrer(f"Validation de {nom}")
    return True

# Programme principal
convertir_fichier("rapport.csv")
valider_fichier("rapport.csv")

# On veut consulter tout le journal ici
journal1 = Journal()
journal2 = Journal()
print(f"Nombre de messages enregistrés : {journal1.nb_messages()}")
journal1.afficher()

#suppresion des messages

journal1.vider()
print(f"Nombre de messages enregistrés : {journal1.nb_messages()}")

test_identite = (journal1 is journal2) 

print(f"journal1 et journal2 sont la même instance : {test_identite}")

