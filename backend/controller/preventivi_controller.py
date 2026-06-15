from flask import Blueprint, request, jsonify
from service import preventivi_service
from exception.app_exception import AppException
import traceback


preventivi_bp = Blueprint("preventivi", __name__)


@preventivi_bp.route("", methods=["GET", "POST"])
def gestisci_preventivi():
    
    if request.method == "POST":
        try:
            data = request.get_json()
            if not data:
                return jsonify({"message": "Nessun dato ricevuto"}), 400
            
            new_prev = preventivi_service.create(data)
            return jsonify({
                "message": "Preventivo creato con successo",
                "preventivo": new_prev.to_dict()
            }), 201
            
        except AppException as e:
            return jsonify({"message": e.message}), e.status_code
        except Exception as e:
            traceback.print_exc()
            return jsonify({"message": "Errore interno server", "error": str(e)}), 500

    #  Recupero storico preventivi
    elif request.method == "GET":
        try:
            lista_preventivi = preventivi_service.get_all()
            return jsonify([p.to_dict() for p in lista_preventivi]), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify({"message": "Errore durante il recupero dello storico"}), 500

    return jsonify({"message": "Metodo non supportato"}), 405

#  (Eliminazione) 
@preventivi_bp.route("/<int:id_preventivo>", methods=["DELETE"])
def elimina_preventivo(id_preventivo):
    try:
       
        successo = preventivi_service.delete(id_preventivo)
        if successo:
            return jsonify({"message": "Preventivo eliminato con successo"}), 200
        else:
            return jsonify({"message": "Preventivo non trovato"}), 404
            
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": "Errore interno durante l'eliminazione", "error": str(e)}), 500

