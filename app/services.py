from app.models import Configuration, PValue, PInfo


def get_params_for_config(config_name):
    c = Configuration.objects(name=config_name).first()
    pvalues = PValue.objects(config=c.id)

    return pvalues
