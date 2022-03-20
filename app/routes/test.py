from flask import Blueprint, render_template, jsonify
from app.models import Configuration

test_bp = Blueprint('test', __name__)


@test_bp.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


# Example adding a new document to a DB collection
@test_bp.route("/test")
def test():
    import random
    import string
    conf = Configuration()
    conf.name = ''.join((random.choice(string.ascii_lowercase) for x in range(10)))
    conf.description = ''.join((random.choice(string.ascii_lowercase) for x in range(20)))
    from datetime import date
    conf.dateCreated = date.today()
    conf.dateModified = date.today()
    conf.showOnAdmin = True
    conf.save()

    configs = Configuration.objects()
    return jsonify(configs), 200
