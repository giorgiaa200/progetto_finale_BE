from exception.app_exception import AppException
from repository.motore_repository import MotoreRepository 
from model.motore import Motore

# Istanzia la classe
repo = MotoreRepository()

def create(data):
    
    # 1. Validazione input
    _validate_motore(data)
    
    # 2. Creazione istanza
    nuovo_motore = Motore(
        nome=data["nome"],
        prezzo=float(data["prezzo"]),
        id_modello=data["id_modello"]
    )
    
    # 3. Salvataggio
    return repo.create(nuovo_motore)

def get_all():
    
    return repo.get_all()

def get_by_id(id_motore):
    
    motore = repo.get_by_id(id_motore)
    if not motore:
        raise AppException(f"Motore con ID {id_motore} non trovato", 404)
    return motore

def get_by_modello(id_modello):
    
    # Esegue la ricerca tramite il repository
    motori = repo.get_by_modello(id_modello)
    
    # Nota: Se non ci sono motori, il repository restituisce una lista vuota.
    # Questo è un comportamento corretto, non serve sollevare un'eccezione 404.
    return motori

def _validate_motore(data):
    """Verifica che i campi siano presenti e validi."""
    campi_obbligatori = ["nome", "prezzo", "id_modello"]
    for campo in campi_obbligatori:
        if campo not in data:
            raise AppException(f"Campo '{campo}' obbligatorio!", 400)
    
    try:
        # Verifica che il prezzo sia un valore numerico valido e non negativo
        if float(data["prezzo"]) < 0:
            raise ValueError
    except (ValueError, TypeError):
        raise AppException("Il prezzo deve essere un numero positivo!", 400)