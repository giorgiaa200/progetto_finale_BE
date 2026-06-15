from repository.modello_repository import ModelloRepository # Importazione corretta
from model.modello import Modello
from exception.app_exception import AppException

# Istanziamo il repository
modello_repository = ModelloRepository()

def create(data):
    
    
    _validate_modello(data)

   
    nuovo_modello = Modello(
        nome=data["nome"], 
        prezzo=float(data["prezzo"])
    )

    #  Salvataggio tramite repository
    return modello_repository.add(nuovo_modello)

def get_all():
    
    return modello_repository.get_all()

def get_by_id(modello_id):
    
    modello = modello_repository.get_by_id(modello_id)
    if modello is None:
        raise AppException(f"Modello con ID {modello_id} non trovato!", 404)
    return modello

def _validate_modello(data):
    
    # Controllo campi obbligatori
    for campo in ["nome", "prezzo"]:
        if campo not in data:
            raise AppException(f"Campo '{campo}' obbligatorio!", 400)
    
    # Validazione stringa vuota
    if len(str(data["nome"]).strip()) == 0:
        raise AppException("Il nome del modello non può essere vuoto!", 400)
    
    # Validazione numerica del prezzo
    try:
        if float(data["prezzo"]) < 0:
            raise ValueError
    except (ValueError, TypeError):
        raise AppException("Il prezzo deve essere un numero positivo!", 400)