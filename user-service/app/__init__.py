from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes import user_bp
    app.register_blueprint(user_bp)
    return app


