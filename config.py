import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    MONGODB_SETTINGS = {'host': os.environ.get('MONGO_URI')}

    # TODO: fix this
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'password'
    TEMPLATES_AUTO_RELOAD = True

    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
