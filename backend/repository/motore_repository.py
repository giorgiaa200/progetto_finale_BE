# Importiamo SessionLocal e lo rinominiamo in Session per coerenza
from database import SessionLocal as Session
from model.motore import Motore

class MotoreRepository:
    def create(self, motore):
        
        session = Session()
        try:
            session.add(motore)
            session.commit()
            session.refresh(motore) # Aggiorna l'oggetto con l'ID generato dal DB
            return motore
        except Exception as e:
            session.rollback() # Annulla le modifiche in caso di errore
            raise e
        finally:
            session.close() # Chiude sempre la sessione

    def get_all(self):
        
        session = Session()
        try:
            return session.query(Motore).all()
        finally:
            session.close()

    def get_by_id(self, id_motore):
        
        session = Session()
        try:
            return session.query(Motore).filter(Motore.id_motore == id_motore).first()
        finally:
            session.close()

    def get_by_modello(self, id_modello):
        
        session = Session()
        try:
            # Filtra i motori in base alla colonna id_modello
            return session.query(Motore).filter(Motore.id_modello == id_modello).all()
        finally:
            session.close()