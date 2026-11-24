# journal.py

class Journal:
    def __init__(self):
        self._messages = []

    def enregistrer(self, message: str) -> None:
        self._messages.append(message)

    def afficher(self) -> None:
        for msg in self._messages:
            print(msg)

    def nb_messages(self) -> int:
        return len(self._messages)