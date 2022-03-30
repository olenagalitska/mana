from flask import Blueprint, render_template, jsonify
from app.models import PInfo
import json

test_bp = Blueprint('test', __name__)

@test_bp.route('/fill')
def fill_in_pinfo():
    f = open('app/routes/pinfos.json')
    data = json.load(f)

    for item in data:
        PInfo(**item).save()

    return render_template('index.html')

# Example adding a new document to a DB collection
@test_bp.route("/test")
def test():
    import random
    import string
    pinfo = PInfo()
    pinfo.name = ''.join((random.choice(string.ascii_lowercase) for x in range(10)))
    pinfo.info = ''.join((random.choice(string.ascii_lowercase) for x in range(20)))
    pinfo.control_type = 'SLIDER'
    pinfo.save()

    pinfos = PInfo.objects()
    return jsonify(pinfos), 200
