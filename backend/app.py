from flask import Flask, jsonify
from flask_cors import CORS
from init_db import setup_database
from controller.modello_controller import modello_bp
from controller.motore_controller import motore_bp
from controller.preventivi_controller import preventivi_bp
from controller.utenti_controller import utenti_bp

def create_app():
    app = Flask(__name__)
    
    
    CORS(app)

    # Inizializzazione Database
    try:
        
        setup_database()
        print("Database pronto.")
    except Exception as e:
        print(f"Errore critico durante l'inizializzazione del DB: {e}")

    # Registrazione dei Blueprint
    app.register_blueprint(modello_bp, url_prefix='/api/modelli')
    app.register_blueprint(motore_bp, url_prefix='/api/motori')
    app.register_blueprint(preventivi_bp, url_prefix='/api/preventivi')
    app.register_blueprint(utenti_bp, url_prefix='/api/utenti')

    @app.route('/', methods=['GET'])
    def home():
        return jsonify({"status": "online", "message": "Il backend del configuratore è attivo"})

    return app

if __name__ == '__main__':
    app = create_app()
    # Il debug=True ti permette di vedere l'errore 500 dettagliato nel terminale
    app.run(debug=True, port=5000)