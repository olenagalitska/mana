from flask import Blueprint, jsonify
from app.models import PInfo
from flask import request

pinfo_bp = Blueprint('pinfo', __name__)


@pinfo_bp.route('/api/pinfos')
def get_configurations():
    pinfo = PInfo.objects()
    return jsonify(pinfo), 200


@pinfo_bp.route('/api/pinfos/<name>')
def get_configuration_by(name: str):
    pinfo = PInfo.objects(name=name).first()
    return jsonify(pinfo), 200


@pinfo_bp.route('/api/pinfos', methods=['POST'])
def add_configuration():
    body = request.get_json()
    pinfo = PInfo(**body).save()
    return jsonify(pinfo), 200


@pinfo_bp.route('/api/pinfos/<name>', methods=['PUT'])
def update_movie(name: str):
    body = request.get_json()
    pinfo = PInfo.objects.get_or_404(name=name)
    pinfo.update(**body)
    return jsonify(pinfo.name), 200


@pinfo_bp.route('/api/pinfos/<name>', methods=['DELETE'])
def delete_movie(name: str):
    pinfo = PInfo.objects.get_or_404(name=name)
    pinfo.delete()
    return jsonify(pinfo.name), 200

