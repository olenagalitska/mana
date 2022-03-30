from flask import Blueprint, jsonify
from app.models import PInfo, PValue
from flask import request

pinfo_bp = Blueprint('pinfo', __name__)


@pinfo_bp.route('/api/pinfos')
def get_pinfos():
    pinfo = PInfo.objects()
    return jsonify(pinfo), 200


@pinfo_bp.route('/api/pinfos/<name>')
def get_pinfo(name: str):
    pinfo = PInfo.objects(name=name).first()
    return jsonify(pinfo), 200


@pinfo_bp.route('/api/pinfos', methods=['POST'])
def add_pinfo():
    body = request.get_json()
    pinfo = PInfo(**body).save()
    return jsonify(pinfo), 200


@pinfo_bp.route('/api/pinfos/<name>', methods=['PUT'])
def update_pinfo(name: str):
    body = request.get_json()
    pinfo = PInfo.objects.get_or_404(name=name)
    pinfo.update(**body)
    return jsonify(pinfo.name), 200


@pinfo_bp.route('/api/pinfos/<name>', methods=['DELETE'])
def delete_pinfo(name: str):
    pinfo = PInfo.objects(name=name).first()
    pinfo.delete()

    pvalues = PValue.objects(pinfo=pinfo)
    pvalues.delete()
    return jsonify(pinfo.name), 200

