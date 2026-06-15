#SQLAlchemy traduce oggetti Python in tabelle SQL. Per farlo, deve sapere che tipo di "dati" andranno nelle colonne.
from sqlalchemy import Column, Integer, String, Float
# Importiamo 'relationship' per gestire il collegamento tra la tabella modelli e motori
from sqlalchemy.orm import relationship

from database import Base

class Modello(Base):
    __tablename__ = 'modelli'
    
    id_modello = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    prezzo = Column(Float, nullable=False)
    
    
    # Diciamo al database: un modello può essere legato a tanti motori diversi.
    # back_populates="modello" crea un collegamento inverso (dal motore verso il modello).
    # cascade="all, delete-orphan" è la "regola di pulizia": se elimino un modello, elimina anche tutti i motori a lui collegati.
    motori = relationship("Motore", back_populates="modello", cascade="all, delete-orphan")


   #def to_dict : Serve a creare un dizionario
   #self ; Serve a leggere i dati specifici dell'oggetto (in questo caso modello) su cui si opera
    def to_dict(self):
        
        data = {
            "id_modello": self.id_modello,
            "nome": self.nome,
            "prezzo": self.prezzo
        }
        
        # Verifica se la relazione 'motori' è già stata caricata nella sessione
        
        if "motori" in self.__dict__:
            data["motori"] = [m.id_motore for m in self.motori]
        else:
            data["motori"] = []
            
        return data