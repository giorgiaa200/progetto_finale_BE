from database import SessionLocal, Base, engine
from model.utenti import Utente
from model.modello import Modello
from model.motore import Motore
from model.preventivi import Preventivo
from werkzeug.security import generate_password_hash

def setup_database():
    print("--- Inizializzazione Database in corso ---")
    
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    
    if session.query(Utente).first():
        print("Database già popolato. Operazione annullata.")
        session.close()
        return

    # 1. Inserimento Modelli
    print("Inserimento modelli...")
    modelli = [
        Modello(id_modello=1, nome="Fiat 500", prezzo=16000.0),
        Modello(id_modello=2, nome="Alfa Romeo Giulia", prezzo=48000.0),
        Modello(id_modello=3, nome="Lancia Ypsilon", prezzo=18500.0),
        Modello(id_modello=4, nome="Ferrari 296 GTB", prezzo=270000.0),
        Modello(id_modello=5, nome="Lamborghini Revuelto", prezzo=500000.0),
        Modello(id_modello=6, nome="Maserati Grecale", prezzo=75000.0),
        Modello(id_modello=7, nome="Fiat Panda", prezzo=14000.0),
        Modello(id_modello=8, nome="Jeep Avenger", prezzo=26000.0),
        Modello(id_modello=9, nome="Pagani Utopia", prezzo=2500000.0),
        Modello(id_modello=10, nome="Lamborghini Huracán", prezzo=220000.0)
    ]
    session.add_all(modelli)
    session.commit()

    # 2. Inserimento Utenti
    print("Inserimento 20 utenti...")
    utenti = []
    for i in range(1, 21):
        ruolo = 'amministratore' if i <= 3 else 'utente'
        u = Utente(
            nome=f"Utente {i}",
            email=f"utente{i}@esempio.it",
            password=generate_password_hash("password123"),
            ruolo=ruolo
        )
        utenti.append(u)
    session.add_all(utenti)
    session.commit()

    # 3. Inserimento Motori (collegati agli ID dei modelli sopra)
    print("Inserimento motori...")
    motori = [
        Motore(nome="Benzina 1.0", prezzo=1500.0, id_modello=1),
         Motore(nome="Benzina 1.0", prezzo=1500.0, id_modello=2),
          Motore(nome="Benzina 1.0", prezzo=1500.0, id_modello=3),
           Motore(nome="Benzina 1.0", prezzo=1500.0, id_modello=4),
            Motore(nome="Benzina 1.0", prezzo=1500.0, id_modello=5),
             Motore(nome="Benzina 1.0", prezzo=1500.0, id_modello=6),
              Motore(nome="Benzina 1.0", prezzo=1500.0, id_modello=7),
               Motore(nome="Benzina 1.0", prezzo=1500.0, id_modello=8),
                Motore(nome="Benzina 1.0", prezzo=1500.0, id_modello=9),
                 Motore(nome="Benzina 1.0", prezzo=1500.0, id_modello=10),
        Motore(nome="Elettrico 150kW", prezzo=8000.0, id_modello=1),
        Motore(nome="Elettrico 150kW", prezzo=8000.0, id_modello=2),
        Motore(nome="Elettrico 150kW", prezzo=8000.0, id_modello=3),
        Motore(nome="Elettrico 150kW", prezzo=8000.0, id_modello=4),
        Motore(nome="Elettrico 150kW", prezzo=8000.0, id_modello=5),
        Motore(nome="Elettrico 150kW", prezzo=8000.0, id_modello=6),
        Motore(nome="Elettrico 150kW", prezzo=8000.0, id_modello=7),
        Motore(nome="Elettrico 150kW", prezzo=8000.0, id_modello=8),
        Motore(nome="Elettrico 150kW", prezzo=8000.0, id_modello=9),
        Motore(nome="Elettrico 150kW", prezzo=8000.0, id_modello=10),

        Motore(nome="Diesel 1.6", prezzo=2500.0, id_modello=1),
        Motore(nome="Diesel 1.6", prezzo=2500.0, id_modello=2),
        Motore(nome="Diesel 1.6", prezzo=2500.0, id_modello=3),
        Motore(nome="Diesel 1.6", prezzo=2500.0, id_modello=4),
        Motore(nome="Diesel 1.6", prezzo=2500.0, id_modello=5),
        Motore(nome="Diesel 1.6", prezzo=2500.0, id_modello=6),
        Motore(nome="Diesel 1.6", prezzo=2500.0, id_modello=7),
        Motore(nome="Diesel 1.6", prezzo=2500.0, id_modello=8),
        Motore(nome="Diesel 1.6", prezzo=2500.0, id_modello=9),
        Motore(nome="Diesel 1.6", prezzo=2500.0, id_modello=10),
        

        Motore(nome="Ibrido 1.8", prezzo=4000.0, id_modello=1),
        Motore(nome="Ibrido 1.8", prezzo=4000.0, id_modello=2),
        Motore(nome="Ibrido 1.8", prezzo=4000.0, id_modello=3),
        Motore(nome="Ibrido 1.8", prezzo=4000.0, id_modello=4),
        Motore(nome="Ibrido 1.8", prezzo=4000.0, id_modello=5),
        Motore(nome="Ibrido 1.8", prezzo=4000.0, id_modello=6),
        Motore(nome="Ibrido 1.8", prezzo=4000.0, id_modello=7),
        Motore(nome="Ibrido 1.8", prezzo=4000.0, id_modello=8),
        Motore(nome="Ibrido 1.8", prezzo=4000.0, id_modello=9),
        Motore(nome="Ibrido 1.8", prezzo=4000.0, id_modello=10),

        Motore(nome="Ibrido Plug-in", prezzo=5500.0, id_modello=1),
        Motore(nome="Ibrido Plug-in", prezzo=5500.0, id_modello=2),
        Motore(nome="Ibrido Plug-in", prezzo=5500.0, id_modello=3),
        Motore(nome="Ibrido Plug-in", prezzo=5500.0, id_modello=4),
        Motore(nome="Ibrido Plug-in", prezzo=5500.0, id_modello=5),
        Motore(nome="Ibrido Plug-in", prezzo=5500.0, id_modello=6),
        Motore(nome="Ibrido Plug-in", prezzo=5500.0, id_modello=7),
        Motore(nome="Ibrido Plug-in", prezzo=5500.0, id_modello=8),
        Motore(nome="Ibrido Plug-in", prezzo=5500.0, id_modello=9),
        Motore(nome="Ibrido Plug-in", prezzo=5500.0, id_modello=10),

        Motore(nome="Diesel 2.0 Turbo", prezzo=3500.0, id_modello=1),
        Motore(nome="Diesel 2.0 Turbo", prezzo=3500.0, id_modello=2),
        Motore(nome="Diesel 2.0 Turbo", prezzo=3500.0, id_modello=3),
        Motore(nome="Diesel 2.0 Turbo", prezzo=3500.0, id_modello=4),
        Motore(nome="Diesel 2.0 Turbo", prezzo=3500.0, id_modello=5),
        Motore(nome="Diesel 2.0 Turbo", prezzo=3500.0, id_modello=6),
        Motore(nome="Diesel 2.0 Turbo", prezzo=3500.0, id_modello=7),
        Motore(nome="Diesel 2.0 Turbo", prezzo=3500.0, id_modello=8),
        Motore(nome="Diesel 2.0 Turbo", prezzo=3500.0, id_modello=9),
        Motore(nome="Diesel 2.0 Turbo", prezzo=3500.0, id_modello=10),

        Motore(nome="Termico V6 Sport", prezzo=6000.0, id_modello=1),
        Motore(nome="Termico V6 Sport", prezzo=6000.0, id_modello=2),
        Motore(nome="Termico V6 Sport", prezzo=6000.0, id_modello=3),
        Motore(nome="Termico V6 Sport", prezzo=6000.0, id_modello=4),
        Motore(nome="Termico V6 Sport", prezzo=6000.0, id_modello=5),
        Motore(nome="Termico V6 Sport", prezzo=6000.0, id_modello=6),
        Motore(nome="Termico V6 Sport", prezzo=6000.0, id_modello=7),
        Motore(nome="Termico V6 Sport", prezzo=6000.0, id_modello=8),
        Motore(nome="Termico V6 Sport", prezzo=6000.0, id_modello=9),
        Motore(nome="Termico V6 Sport", prezzo=6000.0, id_modello=10),

        Motore(nome="Elettrico Performance", prezzo=12000.0, id_modello=1),
        Motore(nome="Elettrico Performance", prezzo=12000.0, id_modello=2),
        Motore(nome="Elettrico Performance", prezzo=12000.0, id_modello=3),
        Motore(nome="Elettrico Performance", prezzo=12000.0, id_modello=4),
        Motore(nome="Elettrico Performance", prezzo=12000.0, id_modello=5),
        Motore(nome="Elettrico Performance", prezzo=12000.0, id_modello=6),
        Motore(nome="Elettrico Performance", prezzo=12000.0, id_modello=7),
        Motore(nome="Elettrico Performance", prezzo=12000.0, id_modello=8),
        Motore(nome="Elettrico Performance", prezzo=12000.0, id_modello=9),
        Motore(nome="Elettrico Performance", prezzo=12000.0, id_modello=10),
        
    ]
    session.add_all(motori)
    session.commit()

    session.close()
    print("--- Setup completato con successo! ---")

if __name__ == "__main__":
    setup_database()