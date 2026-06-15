from database import SessionLocal
from model.preventivi import Preventivo
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError

class PreventivoRepository:
   

    def create(self, preventivo):
        
        with SessionLocal() as session:
            try:
                session.add(preventivo)
                session.commit()
                session.refresh(preventivo)
                session.expunge(preventivo)  # Rende l'oggetto indipendente dalla sessione chiusa
                return preventivo
            except SQLAlchemyError as e:
                session.rollback()
                raise e

    def get_all(self):
        
        with SessionLocal() as session:
            preventivi = session.query(Preventivo).options(
                joinedload(Preventivo.utente),
                joinedload(Preventivo.modello),
                joinedload(Preventivo.motore)
            ).order_by(Preventivo.data_creazione.desc()).all()
            
            # expunge_all per rendere tutti gli oggetti utilizzabili fuori dalla sessione
            session.expunge_all()
            return preventivi

    def get_by_id(self, id_preventivo):
        
        with SessionLocal() as session:
            preventivo = session.query(Preventivo).options(
                joinedload(Preventivo.utente),
                joinedload(Preventivo.modello),
                joinedload(Preventivo.motore)
            ).filter(Preventivo.id_preventivo == id_preventivo).first()
            
            if preventivo:
                session.expunge(preventivo)
            return preventivo

    def delete(self, id_preventivo):
        
        with SessionLocal() as session:
            try:
                preventivo = session.query(Preventivo).filter(Preventivo.id_preventivo == id_preventivo).first()
                if preventivo:
                    session.delete(preventivo)
                    session.commit()
                    return True
                return False
            except SQLAlchemyError as e:
                session.rollback()
                raise e