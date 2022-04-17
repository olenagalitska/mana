from flask import Blueprint, render_template, session, redirect
from app.models import PInfo, Configuration
from app.services import get_params_for_config
import config

webapp_bp = Blueprint('webapp', __name__)


# set admin attr for session
@webapp_bp.before_request
def before_request():
    if "admin" not in session:
        session["admin"] = False
    return None


# home page
@webapp_bp.route('/')
def home():
    return render_template('index.html')


# search for a name in configurations
@webapp_bp.route('/search/<name>')
def search(name: str):
    results = Configuration.objects(name=name)
    return render_template('search.html',
                           name=name,
                           results=results)


# list all configurations
@webapp_bp.route('/configurations')
def configurations():
    all_configurations = Configuration.objects()

    is_admin = session["admin"]
    admin_configurations = []
    if is_admin:
        admin_configurations = Configuration.objects(showOnAdmin=True)
    return render_template('configurations.html',
                           isAdmin=is_admin,
                           all_configurations=all_configurations,
                           admin_configurations=admin_configurations)


# get concrete configuration by name
@webapp_bp.route('/configurations/<name>')
def configuration(name: str):
    found_config = Configuration.objects(name=name).first()
    pvalues_for_config = get_params_for_config(name)
    return render_template('configuration.html',
                           isAdmin=session["admin"],
                           config=found_config,
                           pvalues=pvalues_for_config)


# add new configuration
@webapp_bp.route('/new_configuration')
def new_configuration():
    available_pinfos = PInfo.objects()
    return render_template('new_configuration.html',
                           pinfos=available_pinfos)


# get list of all available parameters (on admin)
@webapp_bp.route('/parameters')
def admin_parameters():
    all_parameters = PInfo.objects()
    is_admin = session["admin"]
    return render_template('parameters.html',
                           isAdmin=is_admin,
                           parameters=all_parameters)


# add new parameter from admin
@webapp_bp.route('/new_parameter')
def new_parameter():
    return render_template('new_parameter.html')


# ADMIN MANAGEMENT


# sign in as admin
@webapp_bp.route('/signin/<password>')
def sign_in(password: str):
    if password == config.Config.ADMIN_PASSWORD:
        session["admin"] = True
        return redirect("/")
    else:
        return


# sign out from admin
@webapp_bp.route('/signout')
def sign_out():
    session["admin"] = False
    return redirect("/")
