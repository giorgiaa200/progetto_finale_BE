import requests
import random

BASE_URL = "http://127.0.0.1:5000/api"

# --- CONFIGURAZIONE INIZIALE ---
lista_modelli = [
    {"nome": "Fiat 500", "prezzo": 16000.00},
    {"nome": "Alfa Romeo Giulia", "prezzo": 48000.00},
    {"nome": "Lancia Ypsilon", "prezzo": 18500.00},
    {"nome": "Ferrari 296 GTB", "prezzo": 270000.00},
    {"nome": "Lamborghini Revuelto", "prezzo": 500000.00},
    {"nome": "Maserati Grecale", "prezzo": 75000.00},
    {"nome": "Fiat Panda", "prezzo": 14000.00},
    {"nome": "Jeep Avenger", "prezzo": 26000.00},
    {"nome": "Pagani Utopia", "prezzo": 2500000.00},
    {"nome": "Lamborghini Huracán", "prezzo": 220000.00}
]

mappa_modelli = {}

# --- 1. CARICAMENTO MODELLI ---
print("--- Caricamento modelli in corso... ---")
for m in lista_modelli:
    risposta = requests.post(f"{BASE_URL}/modelli/", json=m)
    if risposta.status_code == 201:
        dati_risposta = risposta.json()
        id_assegnato = dati_risposta.get("id_modello")
        mappa_modelli[m["nome"]] = id_assegnato
        print(f"✅ Successo: {m['nome']} aggiunto (ID: {id_assegnato})")
    else:
        print(f"❌ Errore {risposta.status_code} per {m['nome']}: {risposta.text}")

# --- 2. CARICAMENTO MOTORI ---
lista_motori = [
    {"nome": "Motore Termico 1.2", "prezzo": 1500.0, "id_modello": mappa_modelli.get("Fiat 500")},
    {"nome": "Motore Gas GPL", "prezzo": 1800.0, "id_modello": mappa_modelli.get("Fiat 500")},
    {"nome": "Motore Diesel 2.0", "prezzo": 2500.0, "id_modello": mappa_modelli.get("Fiat 500")},
    {"nome": "Motore Elettrico 150kW", "prezzo": 4000.0, "id_modello": mappa_modelli.get("Fiat 500")},
    {"nome": "Motore Ibrido Plug-in", "prezzo": 3500.0, "id_modello": mappa_modelli.get("Fiat 500")},
    {"nome": "Motore Termico 1.2", "prezzo": 1500.0, "id_modello": mappa_modelli.get("Alfa Romeo Giulia")},
    {"nome": "Motore Gas GPL", "prezzo": 1800.0, "id_modello": mappa_modelli.get("Alfa Romeo Giulia")},
    {"nome": "Motore Diesel 2.0", "prezzo": 2500.0, "id_modello": mappa_modelli.get("Alfa Romeo Giulia")},
    {"nome": "Motore Elettrico 150kW", "prezzo": 4000.0, "id_modello": mappa_modelli.get("Alfa Romeo Giulia")},
    {"nome": "Motore Ibrido Plug-in", "prezzo": 3500.0, "id_modello": mappa_modelli.get("Alfa Romeo Giulia")},
    {"nome": "Motore Termico 1.2", "prezzo": 1500.0, "id_modello": mappa_modelli.get("Lancia Ypsilon")},
    {"nome": "Motore Gas GPL", "prezzo": 1800.0, "id_modello": mappa_modelli.get("Lancia Ypsilon")},
    {"nome": "Motore Diesel 2.0", "prezzo": 2500.0, "id_modello": mappa_modelli.get("Lancia Ypsilon")},
    {"nome": "Motore Elettrico 150kW", "prezzo": 4000.0, "id_modello": mappa_modelli.get("Lancia Ypsilon")},
    {"nome": "Motore Ibrido Plug-in", "prezzo": 3500.0, "id_modello": mappa_modelli.get("Lancia Ypsilon")},
    {"nome": "Motore Termico 1.2", "prezzo": 1500.0, "id_modello": mappa_modelli.get("Ferrari 296 GTB")},
    {"nome": "Motore Gas GPL", "prezzo": 1800.0, "id_modello": mappa_modelli.get("Ferrari 296 GTB")},
    {"nome": "Motore Diesel 2.0", "prezzo": 2500.0, "id_modello": mappa_modelli.get("Ferrari 296 GTB")},
    {"nome": "Motore Elettrico 150kW", "prezzo": 4000.0, "id_modello": mappa_modelli.get("Ferrari 296 GTB")},
    {"nome": "Motore Ibrido Plug-in", "prezzo": 3500.0, "id_modello": mappa_modelli.get("Ferrari 296 GTB")},
    {"nome": "Motore Termico 1.2", "prezzo": 1500.0, "id_modello": mappa_modelli.get("Lamborghini Revuelto")},
    {"nome": "Motore Gas GPL", "prezzo": 1800.0, "id_modello": mappa_modelli.get("Lamborghini Revuelto")},
    {"nome": "Motore Diesel 2.0", "prezzo": 2500.0, "id_modello": mappa_modelli.get("Lamborghini Revuelto")},
    {"nome": "Motore Elettrico 150kW", "prezzo": 4000.0, "id_modello": mappa_modelli.get("Lamborghini Revuelto")},
    {"nome": "Motore Ibrido Plug-in", "prezzo": 3500.0, "id_modello": mappa_modelli.get("Lamborghini Revuelto")},
    {"nome": "Motore Termico 1.2", "prezzo": 1500.0, "id_modello": mappa_modelli.get("Maserati Grecale")},
    {"nome": "Motore Gas GPL", "prezzo": 1800.0, "id_modello": mappa_modelli.get("Maserati Grecale")},
    {"nome": "Motore Diesel 2.0", "prezzo": 2500.0, "id_modello": mappa_modelli.get("Maserati Grecale")},
    {"nome": "Motore Elettrico 150kW", "prezzo": 4000.0, "id_modello": mappa_modelli.get("Maserati Grecale")},
    {"nome": "Motore Ibrido Plug-in", "prezzo": 3500.0, "id_modello": mappa_modelli.get("Maserati Grecale")},
    {"nome": "Motore Termico 1.2", "prezzo": 1500.0, "id_modello": mappa_modelli.get("Fiat Panda")},
    {"nome": "Motore Gas GPL", "prezzo": 1800.0, "id_modello": mappa_modelli.get("Fiat Panda")},
    {"nome": "Motore Diesel 2.0", "prezzo": 2500.0, "id_modello": mappa_modelli.get("Fiat Panda")},
    {"nome": "Motore Elettrico 150kW", "prezzo": 4000.0, "id_modello": mappa_modelli.get("Fiat Panda")},
    {"nome": "Motore Ibrido Plug-in", "prezzo": 3500.0, "id_modello": mappa_modelli.get("Fiat Panda")},
    {"nome": "Motore Termico 1.2", "prezzo": 1500.0, "id_modello": mappa_modelli.get("Jeep Avenger")},
    {"nome": "Motore Gas GPL", "prezzo": 1800.0, "id_modello": mappa_modelli.get("Jeep Avenger")},
    {"nome": "Motore Diesel 2.0", "prezzo": 2500.0, "id_modello": mappa_modelli.get("Jeep Avenger")},
    {"nome": "Motore Elettrico 150kW", "prezzo": 4000.0, "id_modello": mappa_modelli.get("Jeep Avenger")},
    {"nome": "Motore Ibrido Plug-in", "prezzo": 3500.0, "id_modello": mappa_modelli.get("Jeep Avenger")},
    {"nome": "Motore Termico 1.2", "prezzo": 1500.0, "id_modello": mappa_modelli.get("Pagani Utopia")},
    {"nome": "Motore Gas GPL", "prezzo": 1800.0, "id_modello": mappa_modelli.get("Pagani Utopia")},
    {"nome": "Motore Diesel 2.0", "prezzo": 2500.0, "id_modello": mappa_modelli.get("Pagani Utopia")},
    {"nome": "Motore Elettrico 150kW", "prezzo": 4000.0, "id_modello": mappa_modelli.get("Pagani Utopia")},
    {"nome": "Motore Ibrido Plug-in", "prezzo": 3500.0, "id_modello": mappa_modelli.get("Pagani Utopia")},
    {"nome": "Motore Termico 1.2", "prezzo": 1500.0, "id_modello": mappa_modelli.get("Lamborghini Huracán")},
    {"nome": "Motore Gas GPL", "prezzo": 1800.0, "id_modello": mappa_modelli.get("Lamborghini Huracán")},
    {"nome": "Motore Diesel 2.0", "prezzo": 2500.0, "id_modello": mappa_modelli.get("Lamborghini Huracán")},
    {"nome": "Motore Elettrico 150kW", "prezzo": 4000.0, "id_modello": mappa_modelli.get("Lamborghini Huracán")},
    {"nome": "Motore Ibrido Plug-in", "prezzo": 3500.0, "id_modello": mappa_modelli.get("Lamborghini Huracán")}
]   

print("\n--- Caricamento motori in corso... ---")
for motore in lista_motori:
    if motore["id_modello"] is None: continue
    risposta = requests.post(f"{BASE_URL}/motori/", json=motore)
    if risposta.status_code == 201:
        print(f"✅ Successo: {motore['nome']} aggiunto!")

# --- 3. CARICAMENTO UTENTI ---
nomi_reali = ["Alessandro Rossi", "Giulia Bianchi", "Matteo Verdi", "Sofia Neri", "Luca Esposito",
              "Chiara Romano", "Davide Colombo", "Elena Ricci", "Francesco Marino", "Sara Greco",
              "Roberto Bruno", "Martina Gallo", "Andrea Conti", "Elisa De Luca", "Stefano Costa",
              "Valentina Giordano", "Federico Mancini", "Anna Rinaldi", "Marco Esposito", "Giorgia Moretti"]
lista_id_utenti = [] 

print("\n--- Caricamento 20 Utenti ---")
for nome in nomi_reali:
    utente = {"nome": nome, "email": f"{nome.lower().replace(' ', '.')}@test.it", "password": f"{nome.replace(' ', '')}1"}
    risposta = requests.post(f"{BASE_URL}/utenti", json=utente)
    if risposta.status_code == 201:
        lista_id_utenti.append(risposta.json().get("id"))
        print(f"✅ Creato: {nome}")

# --- 4. CREAZIONE 6 PREVENTIVI ---
print("\n--- Creazione 6 Preventivi ---")
for i in range(1, 7):
    id_utente_scelto = random.choice(lista_id_utenti)
    nome_modello_scelto = random.choice(list(mappa_modelli.keys()))
    id_modello_scelto = mappa_modelli[nome_modello_scelto]
    
    risposta_motori = requests.get(f"{BASE_URL}/motori/?id_modello={id_modello_scelto}")
    if risposta_motori.status_code == 200 and len(risposta_motori.json()) > 0:
        motore_scelto = random.choice(risposta_motori.json())
        payload = {"id_utente": id_utente_scelto, "id_modello": id_modello_scelto, "id_motore": motore_scelto["id_motore"]}
        
        # CHIAMATA POST CORRETTA CON SLASH FINALE
        risposta_prev = requests.post(f"{BASE_URL}/preventivi/", json=payload)
        
        if risposta_prev.status_code == 201:
            print(f"✅ Preventivo {i}: Successo")
        else:
            print(f"❌ Errore Preventivo {i}: {risposta_prev.text}")

# --- 5. VERIFICA ---
print("\n--- Verifica Preventivi ---")
risposta_verifica = requests.get(f"{BASE_URL}/preventivi/")
print(f"✅ Nel database ci sono {len(risposta_verifica.json())} preventivi registrati.")