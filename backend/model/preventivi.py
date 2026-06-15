from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Preventivo(Base):
    __tablename__ = 'preventivi'
    
    id_preventivo = Column(Integer, primary_key=True, autoincrement=True)
    id_utente = Column(Integer, ForeignKey('utenti.id_utente'), nullable=False)
    id_modello = Column(Integer, ForeignKey('modelli.id_modello'), nullable=False)
    id_motore = Column(Integer, ForeignKey('motori.id_motore'), nullable=False)
    prezzo_totale = Column(Float, nullable=False)
    data_creazione = Column(DateTime, default=datetime.utcnow)
    
    # Relazioni
    utente = relationship("Utente", back_populates="preventivi")
    modello = relationship("Modello")
    motore = relationship("Motore")

    def to_dict(self):
       
        return {
            "id_preventivo": self.id_preventivo,
            "id_utente": self.id_utente,
            "id_modello": self.id_modello,
            # Accesso al nome tramite la relazione definita sopra
            "nome_modello": self.modello.nome if self.modello else "Modello non trovato",
            "id_motore": self.id_motore,
            # Accesso al nome tramite la relazione definita sopra
            "nome_motore": self.motore.nome if self.motore else "Motore non trovato",
            "prezzo_totale": self.prezzo_totale,
            "data_creazione": self.data_creazione.isoformat() if self.data_creazione else None
        }