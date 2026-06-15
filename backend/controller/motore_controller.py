from flask import Blueprint, request, jsonify
from service import motore_service
from exception.app_exception import AppException

# Creazione del Blueprint per i motori
motore_bp = Blueprint('motore_bp', __name__)


@motore_bp.route('/', methods=['GET'])
def get_all_motori():
    
    try:
        motori = motore_service.get_all()
        return jsonify([m.to_dict() for m in motori]), 200
    except Exception as e:
        print(f"Errore nel recupero motori: {e}")
        return jsonify({"message": "Errore interno del server"}), 500


@motore_bp.route('/modello/<int:id_modello>', methods=['GET'])
def get_motori_by_modello(id_modello):
    
    try:
        motori = motore_service.get_by_modello(id_modello)
        # Restituisce una lista (anche vuota se non ci sono motori)
        return jsonify([m.to_dict() for m in motori]), 200
    except Exception as e:
        print(f"Errore nel recupero motori per il modello {id_modello}: {e}")
        return jsonify({"message": "Errore interno del server"}), 500


@motore_bp.route('/<int:id_motore>', methods=['GET'])
def get_motore(id_motore):
    
    try:
        motore = motore_service.get_by_id(id_motore)
        if not motore:
            return jsonify({"message": "Motore non trovato"}), 404
        return jsonify(motore.to_dict()), 200
    except Exception as e:
        print(f"Errore nel recupero del motore {id_motore}: {e}")
        return jsonify({"message": "Errore interno del server"}), 500


@motore_bp.route('/', methods=['POST'])
def add_motore():
    """Salva un nuovo motore nel database."""
    try:
        data = request.get_json()
        # Verifica che tutti i campi obbligatori siano presenti
        if not data or not all(k in data for k in ('nome', 'prezzo', 'id_modello')):
            return jsonify({"message": "Dati mancanti: nome, prezzo o id_modello richiesti"}), 400
        
        nuovo_motore = motore_service.create(data)
        return jsonify({"message": "Motore creato con successo", "motore": nuovo_motore.to_dict()}), 201
    except AppException as e:
        # Gestione errori personalizzati (es. validazioni)
        return jsonify({"message": str(e)}), e.status_code
    except Exception as e:
        print(f"Errore durante la creazione del motore: {e}")
        return jsonify({"message": "Errore interno del server"}), 500