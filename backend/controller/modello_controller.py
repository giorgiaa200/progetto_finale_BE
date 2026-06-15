from flask import Blueprint, jsonify, request
from service import modello_service
from exception.app_exception import AppException


modello_bp = Blueprint("modello", __name__)


@modello_bp.route("/", methods=["GET"])
def get_modelli():
    
    try:
        modelli = modello_service.get_all()
        
        return jsonify([m.to_dict() for m in modelli]), 200
    except Exception as e:
        return jsonify({"message": "Errore nel recupero dei modelli", "error": str(e)}), 500


@modello_bp.route("/<int:id>", methods=["GET"])
def get_modello(id):
    
    try:
        modello = modello_service.get_by_id(id)
        if not modello:
            return jsonify({"message": f"Modello con ID {id} non trovato"}), 404
        return jsonify(modello.to_dict()), 200
    except Exception as e:
        return jsonify({"message": "Errore nel recupero del modello", "error": str(e)}), 500


@modello_bp.route("/", methods=["POST"])
def create_modello():
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "Dati mancanti"}), 400
        
        nuovo_modello = modello_service.create(data)
        return jsonify(nuovo_modello.to_dict()), 201
    except AppException as e:
        return jsonify({"message": e.message}), e.status_code
    except Exception as e:
        return jsonify({"message": "Errore durante la creazione", "error": str(e)}), 500