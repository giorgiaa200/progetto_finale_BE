from flask import Blueprint, request, jsonify
from service import utenti_service
from exception.app_exception import AppException
import traceback # Importa traceback per vedere gli errori nel terminale

utenti_bp = Blueprint('utenti_bp', __name__)


@utenti_bp.route('', methods=['POST'], strict_slashes=False)
def register():
    try:
        data = request.get_json()
        print(f"DEBUG: Dati ricevuti: {data}")
        nuovo_utente = utenti_service.create(data)
        
        return jsonify({
            "id": nuovo_utente.id_utente, 
            "message": "Utente registrato con successo!",
            "utente": nuovo_utente.to_dict()
        }), 201

    except AppException as e:
        return jsonify({"message": str(e)}), e.status_code
    except Exception as e:
        traceback.print_exc() # Stampa l'errore reale nel terminale di VS Code
        return jsonify({"message": "Errore interno del server", "error": str(e)}), 500

@utenti_bp.route('/login', methods=['POST'], strict_slashes=False)
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        utente = utenti_service.authenticate(email, password)
        if utente:
            return jsonify({
                "message": "Login effettuato", 
                "user_id": utente.id_utente
            }), 200
        return jsonify({"message": "Credenziali errate"}), 401
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Errore interno del server", "error": str(e)}), 500

@utenti_bp.route('/<int:id_utente>', methods=['GET'], strict_slashes=False)
def get_user(id_utente):
    try:
        utente = utenti_service.get_by_id(id_utente)
        return jsonify(utente.to_dict()), 200
    except AppException as e:
        return jsonify({"message": str(e)}), e.status_code
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Errore interno del server", "error": str(e)}), 500