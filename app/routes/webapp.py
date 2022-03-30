from flask import Blueprint, render_template
from app.models import PValue, PInfo, Configuration

webapp_bp = Blueprint('webapp', __name__)


@webapp_bp.route('/')
def home():
    return render_template('index.html')


@webapp_bp.route('/search/<name>')
def search(name: str):
    results = Configuration.objects(name=name)
    return render_template('search.html', name=name, results=results)

@webapp_bp.route('/configurations')
def configurations():
    configurations = Configuration.objects()
    return render_template('configurations.html', configurations=configurations)

@webapp_bp.route('/configurations/<name>')
def configuration(name: str):
    config = Configuration.objects(name=name).first()
    return render_template('configuration.html', config=config)

@webapp_bp.route('/configurations/new')
def new_configuration():
    return render_template('new_configuration.html')