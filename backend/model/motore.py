from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Motore(Base):
    __tablename__ = 'motori'
    id_motore = Column(Integer, primary_key=True)
    nome = Column(String(100))
    prezzo = Column(Float)
    id_modello = Column(Integer, ForeignKey('modelli.id_modello'))
    
    modello = relationship("Modello", back_populates="motori")

    def to_dict(self):
        return {
            "id_motore": self.id_motore,
            "nome": self.nome,
            "prezzo": self.prezzo,
            "id_modello": self.id_modello
        }