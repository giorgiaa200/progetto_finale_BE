from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Utente(Base):
    __tablename__ = 'utenti'
    
    id_utente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    ruolo = Column(String(20), default="utente")
    
    preventivi = relationship("Preventivo", back_populates="utente", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id_utente": self.id_utente,
            "nome": self.nome,
            "email": self.email,
            "ruolo": self.ruolo
        }