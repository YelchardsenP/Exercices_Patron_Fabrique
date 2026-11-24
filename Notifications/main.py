# main.py
from notifications import creer_notification

canaux = ["console", "courriel", "sms"]

destinateur = {"console": "Alice", "courriel": "alice@example.com", "sms": "555-1234"}

for canal in canaux:
    notif = creer_notification(canal)
    notif.envoyer(destinateur[canal], "Votre conversion est terminée.")

print()

try:
    creer_notification("fax")
except ValueError as e:
    print(f"Erreur : {e}")