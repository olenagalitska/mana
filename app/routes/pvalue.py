from flask import Blueprint, jsonify
from app.models import PValue
from flask import request

pvalue_bp = Blueprint('pvalue', __name__)


@pvalue_bp.route('/api/pvalues')
def get_configurations():
    pvalue = PValue.objects()
    return jsonify(pvalue), 200


@pvalue_bp.route('/api/pvalues/<_id>')
def get_configuration_by(_id: str):
    pvalue = PValue.objects(_id=_id).first()
    return jsonify(pvalue), 200


@pvalue_bp.route('/api/pvalues', methods=['POST'])
def add_configuration():
    body = request.get_json()
    pvalue = PValue(**body).save()
    return jsonify(pvalue), 200


@pvalue_bp.route('/api/pvalues/<_id>', methods=['PUT'])
def update_pvalue(_id: str):
    body = request.get_json()
    pvalue = PValue.objects.get_or_404(_id=_id)
    pvalue.update(**body)
    return jsonify(pvalue._id), 200


@pvalue_bp.route('/api/pvalues/<_id>', methods=['DELETE'])
def delete_pvalue(_id: str):
    pvalue = PValue.objects.get_or_404(_id=_id)
    pvalue.delete()
    return jsonify(pvalue._id), 200

