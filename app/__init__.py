import flask
from flask_mongoengine import MongoEngine
from config import Config

db = MongoEngine()


def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes.test import test_bp
    app.register_blueprint(test_bp)

    return app
