from flask import Flask
from .routes import inventory_bp  # Adjust import if needed

def create_app():
    app = Flask(__name__)
    app.register_blueprint(inventory_bp)  # Register the blueprint
    return app

