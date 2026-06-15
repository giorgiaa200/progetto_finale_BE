from database import SessionLocal
from model.modello import Modello
from sqlalchemy.exc import SQLAlchemyError

class ModelloRepository:
    ## Metodo per recuperare tutti i modelli presenti nel database
    def get_all(self):
        
        with SessionLocal() as session:
            return session.query(Modello).all()
        

    # Metodo per cercare un modello specifico tramite il suo ID univoco
    def get_by_id(self, id_modello):
        
        with SessionLocal() as session:
            return session.query(Modello).filter(Modello.id_modello == id_modello).first()
        

    # Metodo per aggiungere un nuovo oggetto modello nel database
    def add(self, modello):
        
        with SessionLocal() as session:
            try:
                session.add(modello)
                session.commit()
                session.refresh(modello)
                return modello
            except SQLAlchemyError as e:
                session.rollback()
                raise e
    

    # Metodo per eliminare un modello esistente tramite il suo ID
    def delete(self, id_modello):
        
        with SessionLocal() as session:
            try:
                modello = session.query(Modello).filter(Modello.id_modello == id_modello).first()
                if modello:
                    session.delete(modello)
                    session.commit()
                    return True
                return False
            except SQLAlchemyError as e:
                session.rollback()
                raise e