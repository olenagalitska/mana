from flask import Blueprint, render_template
from app.models import PValue, PInfo, Configuration
from app.services import get_params_for_config

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
    pvalues = get_params_for_config(name)
    print(pvalues)
    return render_template('configuration.html', config=config, pvalues=pvalues)


@webapp_bp.route('/configurations/new')
def new_configuration():
    return render_template('new_configuration.html')


@webapp_bp.route('/admin/configurations')
def admin_configurations():
    configs = Configuration.objects(showOnAdmin=True)
    return render_template('admin.html', config=True, configurations=configs)


@webapp_bp.route('/admin/parameters')
def admin_parameters():
    params = PInfo.objects()
    return render_template('admin.html', config=False, parameters=params)


@webapp_bp.route('/admin/parameters/new')
def new_parameter():
    return render_template('new_parameter.html')
