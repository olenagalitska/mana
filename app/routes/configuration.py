from flask import Blueprint, jsonify
from app.models import Configuration
from flask import request
from datetime import datetime

config_bp = Blueprint('config', __name__)


@config_bp.route('/api/configurations')
def get_configurations():
    configurations = Configuration.objects()
    return jsonify(configurations), 200


@config_bp.route('/api/configurations/<name>')
def get_configuration_by(name: str):
    configuration = Configuration.objects(name=name).first()
    return jsonify(configuration), 200


@config_bp.route('/api/configurations', methods=['POST'])
def add_configuration():
    body = request.get_json()
    date = datetime.now()
    body["dateModified"] = date
    body["dateCreated"] = date
    configuration = Configuration(**body).save()
    return jsonify(configuration), 200


@config_bp.route('/api/configurations/<name>', methods=['PUT'])
def update_configuration(name: str):
    body = request.get_json()
    configuration = Configuration.objects.get_or_404(name=name)
    body["dateModified"] = datetime.now()
    configuration.update(**body)
    return jsonify(configuration.name), 200


@config_bp.route('/api/configurations/<name>', methods=['DELETE'])
def delete_configuration(name: str):
    configuration = Configuration.objects.get_or_404(name=name)
    configuration.delete()
    return jsonify(configuration.name), 200

