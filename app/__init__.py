import flask
from flask_pymongo import PyMongo
from app.config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)

from app import routes

mongodb_client = PyMongo(app)
db = mongodb_client.db


# Example adding a new document to a DB collection
# @app.route("/add_one")
# def add_one():
#     db.tests.insert_one({'title': "test", 'body': "1"})
#     return flask.jsonify(message="success")
