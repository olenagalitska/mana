import flask
from flask_mongoengine import MongoEngine
from config import Config

db = MongoEngine()


def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes.test import test_bp
    from app.routes.configuration import config_bp
    from app.routes.pinfo import pinfo_bp
    from app.routes.pvalue import pvalue_bp
    from app.routes.webapp import webapp_bp

    app.register_blueprint(test_bp)
    app.register_blueprint(config_bp)
    app.register_blueprint(pinfo_bp)
    app.register_blueprint(pvalue_bp)
    app.register_blueprint(webapp_bp)

    return app
