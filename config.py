import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'djfbviehbrkvebdjsuf'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://lena:123@localhost:5432/mana'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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