from flask import Blueprint, render_template, jsonify
from .models import Configuration

routes_bp = Blueprint('routes', __name__)


@routes_bp.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


# Example adding a new document to a DB collection
@routes_bp.route("/test")
def test():
    conf = Configuration()
    conf.name = "First Conf"
    conf.description = "Bla bla bla"
    from datetime import date
    conf.dateCreated = date.today()
    conf.dateModified = date.today()
    conf.showOnAdmin = True
    conf.save()

    configs = Configuration.objects()
    return jsonify(configs), 200
