# journal.py

class Journal:

    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Journal, cls).__new__(cls)
            cls._instance._initialiser()
            return cls._instance
        else:
            return cls._instance
            
    
    
    def _initialiser(self):
        self._messages = []

    def enregistrer(self, message: str) -> None:
        self._messages.append(message)

    def afficher(self) -> None:
        for msg in self._messages:
            print(msg)

    def vider(self) -> None:
        self._messages.clear()
        print("Le journal a été vidé.")


    def nb_messages(self) -> int:
        return len(self._messages)