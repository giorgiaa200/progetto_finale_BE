from repository.utenti_repository import UtenteRepository
from model.utenti import Utente
from exception.app_exception import AppException
from werkzeug.security import generate_password_hash, check_password_hash

repo = UtenteRepository()

def authenticate(email, password):
    # 1. Recupera utente
    utente = repo.get_by_email(email)
    
    # 2. Se l'utente non esiste, restituisce None 
    if not utente:
        return None
    
    # 3. Verifica password (solo se utente esiste)
    if check_password_hash(utente.password, password):
        return utente
    
    return None

def create(data):
    if not all(k in data for k in ('nome', 'email', 'password')):
        raise AppException("Dati mancanti: nome, email e password sono obbligatori", 400)
    
    if repo.get_by_email(data.get('email')):
        raise AppException("Email già registrata", 409)
    
    hashed_password = generate_password_hash(data.get('password'))
    nuovo_utente = Utente(
        nome=data.get('nome'),
        email=data.get('email'),
        password=hashed_password,
        ruolo=data.get('ruolo', 'utente')
    )
    return repo.create(nuovo_utente)