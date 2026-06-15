from database import engine, Base
# Importa tutti i modelli affinché Base li conosca
from model.utenti import Utente
from model.modello import Modello
from model.motore import Motore
from model.preventivi import Preventivo

def reset():
    print("Eliminazione tabelle esistenti...")
    Base.metadata.drop_all(bind=engine)
    print("Ricreazione tabelle...")
    Base.metadata.create_all(bind=engine)
    print("Database resettato con successo!")

if __name__ == "__main__":
    reset()