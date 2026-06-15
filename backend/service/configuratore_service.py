from repository.modello_repository import ModelloRepository
from repository.motore_repository import MotoreRepository
from repository.preventivi_repository import PreventivoRepository
from repository.utenti_repository import UtenteRepository

from exception.app_exception import AppException
from model.preventivi import Preventivo

# Istanziamo le classi per creare gli oggetti repository
modello_repo = ModelloRepository()
motore_repo = MotoreRepository()
preventivi_repo = PreventivoRepository()
utenti_repo = UtenteRepository()

def calcola_preventivo(modello_id, motore_id):
    
    modello = modello_repo.get_by_id(modello_id)
    motore = motore_repo.get_by_id(motore_id)
    
    if not modello:
        raise AppException("Modello non trovato", 404)
    if not motore:
        raise AppException("Motore non trovato", 404)
        
    return modello.prezzo + motore.prezzo 

def crea_e_salva_preventivi(data):
    
    # 1. Verifica esistenza utente
    utente = utenti_repo.get_by_id(data.get("id_utente"))
    if not utente:
        raise AppException("Utente non trovato", 404)
        
    # 2. Calcola prezzo totale
    prezzo_totale = calcola_preventivo(data.get("id_modello"), data.get("id_motore"))
    
    # 3. Crea istanza Preventivo
    nuovo_preventivo = Preventivo(
        id_utente=data.get("id_utente"),
        id_modello=data.get("id_modello"),
        id_motore=data.get("id_motore"),
        prezzo_totale=prezzo_totale
    )
    
    # 4. Salva nel repository usando l'istanza corretta
    return preventivi_repo.create(nuovo_preventivo)

def get_riepilogo_preventivi():
    
    return preventivi_repo.get_all()