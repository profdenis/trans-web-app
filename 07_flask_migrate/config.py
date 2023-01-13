import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or r'sqlite:///contacts.sqlite'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or r'postgresql://webapps:webapps@localhost:5432/denis'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           f'postgresql://webapps:{os.environ.get("DATABASE_PASSWORD")}@localhost:5432/denis'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
