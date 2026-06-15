import requests

BASE_URL = "http://127.0.0.1:5000/api"

# 1. Test GET Modelli
print("--- Test Modelli ---")
modelli = requests.get(f"{BASE_URL}/modelli/").json()
print(f"Modelli trovati: {modelli}")

# 2. Test POST Preventivo 
print("\n--- Test Creazione Preventivo ---")
dati_preventivo = {
    "id_utente": 1, 
    "id_modello": 1, 
    "id_motore": 1
}
response = requests.post(f"{BASE_URL}/preventivi/", json=dati_preventivo)
print(f"Risposta: {response.status_code} - {response.json()}")

# 3. Test GET Preventivi (Lo storico)
print("\n--- Test Storico Preventivi ---")
storico = requests.get(f"{BASE_URL}/preventivi/").json()
print(f"Storico aggiornato: {storico}")