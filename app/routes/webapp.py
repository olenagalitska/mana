from flask import Blueprint, render_template
from app.models import PValue, PInfo, Configuration

webapp_bp = Blueprint('webapp', __name__)


@webapp_bp.route('/')
def home():
    return render_template('index.html')

