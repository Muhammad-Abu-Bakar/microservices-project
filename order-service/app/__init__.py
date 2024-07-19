from flask import Flask
from .routes import order_bp  # Adjust import if needed

def create_app():
    app = Flask(__name__)
    app.register_blueprint(order_bp)  # Register the blueprint
    return app

