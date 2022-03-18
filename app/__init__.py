import flask
from flask_mongoengine import MongoEngine
from config import Config

db = MongoEngine()


def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes import routes_bp
    app.register_blueprint(routes_bp)

    return app
