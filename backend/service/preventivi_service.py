from repository.modello_repository import ModelloRepository
from repository.motore_repository import MotoreRepository
from repository.preventivi_repository import PreventivoRepository
from repository.utenti_repository import UtenteRepository
from model.preventivi import Preventivo
from exception.app_exception import AppException
from database import SessionLocal
from sqlalchemy.orm import joinedload

# Inizializziamo i repository
modello_repo = ModelloRepository()
motore_repo = MotoreRepository()
preventivi_repo = PreventivoRepository()
utenti_repo = UtenteRepository()

def create(data):
    # 1. Validazione tipi
    try:
        id_utente = int(data.get("id_utente"))
        id_modello = int(data.get("id_modello"))
        id_motore = int(data.get("id_motore"))
    except (ValueError, TypeError):
        raise AppException("ID forniti non validi (devono essere numeri)", 400)

    # 2. Recupero entità
    utente = utenti_repo.get_by_id(id_utente)
    modello = modello_repo.get_by_id(id_modello)
    motore = motore_repo.get_by_id(id_motore)
    
    if not utente: raise AppException(f"Utente non trovato con ID {id_utente}", 404)
    if not modello: raise AppException(f"Modello non trovato con ID {id_modello}", 404)
    if not motore: raise AppException(f"Motore non trovato con ID {id_motore}", 404)
    
    # 3. Logica Prezzo
    prezzo_totale = modello.prezzo + motore.prezzo
    
    # 4. Creazione entità
    nuovo_preventivo = Preventivo(
        id_utente=id_utente,
        id_modello=id_modello,
        id_motore=id_motore,
        prezzo_totale=prezzo_totale
    )
    
    # 5. Salvataggio
    session = SessionLocal()
    try:
        session.add(nuovo_preventivo)
        session.commit()
        session.refresh(nuovo_preventivo) 
        
        
        preventivo_finale = session.query(Preventivo)\
            .options(joinedload(Preventivo.modello), joinedload(Preventivo.motore))\
            .filter(Preventivo.id_preventivo == nuovo_preventivo.id_preventivo)\
            .first()
            
        return preventivo_finale
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_all():
    
    return preventivi_repo.get_all()

def delete(id_preventivo):
   
    if not id_preventivo:
        raise AppException("ID preventivo mancante", 400)
    
    # Eseguo la chiamata al repository in sicurezza
    return preventivi_repo.delete(id_preventivo)