#create_engine è la funzione  che riceve i comandi Python e li traduce in linguaggio SQL per poi inviarli al database.
from sqlalchemy import create_engine

#session = sessionmaker(bind=engine)sessionmaker è la "fabbrica" (crea sessioni),gestisce le transazioni e il ciclo di vita degli oggetti.
#declarative_base(), crea un oggetto Base. Questo oggetto diventa la "classe genitore" che tutte le tue tabelle devono ereditare.
from sqlalchemy.orm import sessionmaker, declarative_base
#orm:object-relational mapping:una tecnica che mappa automaticamente oggetti dal linguaggio a righe di tabelle in un db


#È la "stringa di connessione". Contiene il tipo di DB (Postgres), le credenziali (utente/password), l'host (localhost) e il nome del database (configuratore_auto).
DATABASE_URL = "postgresql://postgres:Vita%402025@localhost:5432/configuratore_auto"

engine = create_engine(DATABASE_URL)

# SessionLocal --> Factory di sessione, ogni sessione è una conversazione verso il database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



# def init_db():Corrisponde a scrivere le CREATE TABLE per ogni modello elencato
#crea tutte le tabelle nel database basandosi sui modelli registrati
def init_db():
    # Importa qui i modelli 
    import model.utenti
    import model.modello
    import model.motore
    import model.preventivi

    # Base.metadata: Il registro che contiene i progetti di tutte le classi ereditate da Base.
    # create_all: Il comando che "costruisce" fisicamente le tabelle nel database PostgreSQL.
    Base.metadata.create_all(bind=engine)