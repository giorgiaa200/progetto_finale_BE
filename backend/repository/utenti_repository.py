from database import SessionLocal
from model.utenti import Utente
from sqlalchemy.exc import SQLAlchemyError

class UtenteRepository:
    def create(self, utente):
        
        with SessionLocal() as session:
            try:
                session.add(utente)
                session.commit()
                session.refresh(utente)
                session.expunge(utente)
                return utente
            except SQLAlchemyError as e:
                session.rollback()
                raise e

    def get_by_id(self, id_utente):
        
        with SessionLocal() as session:
            
            utente = session.query(Utente).filter(Utente.id_utente == id_utente).first()
            
            if utente:
                # expunge permette di usare l'oggetto utente anche dopo la chiusura della sessione
                session.expunge(utente)
            return utente

    def get_by_email(self, email):
        
        with SessionLocal() as session:
            utente = session.query(Utente).filter(Utente.email == email).first()
            if utente:
                session.expunge(utente)
            return utente