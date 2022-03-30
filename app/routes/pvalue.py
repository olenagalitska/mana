from flask import Blueprint, jsonify
from app.models import PValue
from flask import request

pvalue_bp = Blueprint('pvalue', __name__)


@pvalue_bp.route('/api/pvalues')
def get_configurations():
    pvalue = PValue.objects()
    return jsonify(pvalue), 200


@pvalue_bp.route('/api/pvalues/<_id>')
def get_configuration_by(id: str):
    pvalue = PValue.objects(id=id).first()
    return jsonify(pvalue), 200


@pvalue_bp.route('/api/pvalues', methods=['POST'])
def add_configuration():
    body = request.get_json()
    pvalue = PValue(**body).save()
    return jsonify(pvalue), 200


@pvalue_bp.route('/api/pvalues/<id>', methods=['PUT'])
def update_pvalue(id: str):
    body = request.get_json()
    pvalue = PValue.objects.get_or_404(id=id)
    pvalue.update(**body)
    return 200


@pvalue_bp.route('/api/pvalues/<id>', methods=['DELETE'])
def delete_pvalue(id: str):
    pvalue = PValue.objects(id=id).first()
    pvalue.delete()
    return 200

