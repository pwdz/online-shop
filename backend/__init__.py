from flask import Flask
from .extensions import mongo
from .main import main
import secrets


def create_app(config_object='backend.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    mongo.init_app(app)
    print("Database Connection Established")
    app.register_blueprint(main)
    secret = secrets.token_urlsafe(32)
    app.secret_key = secret

    return app
