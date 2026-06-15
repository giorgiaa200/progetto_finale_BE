from flask import jsonify, request, Blueprint
from service import configuratore_service, modello_service
from service import motore_service
from exception.app_exception import AppException


configuratore_bp = Blueprint("configuratore", __name__)

@configuratore_bp.route("/modelli", methods=["GET"])
def get_modelli():
    modelli = modello_service.get_all()
    return jsonify([m.to_dict() for m in modelli]), 200

@configuratore_bp.route("/motori", methods=["GET"])
def get_motori():
    motori = motore_service.get_all()
    return jsonify([m.to_dict() for m in motori]), 200

@configuratore_bp.route("/preventivo", methods=["POST"])
def create_preventivo():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Nessun dato fornito"}), 400
    try:
        new_prev = configuratore_service.crea_e_salva_preventivo(data)
        return jsonify(new_prev.to_dict()), 201
    except AppException as e:
        return jsonify({"message": e.message}), e.status_code
    except Exception as e:
        return jsonify({"message": "Errore interno del server", "error": str(e)}), 500