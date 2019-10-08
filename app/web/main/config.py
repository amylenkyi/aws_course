import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    PORT = os.getenv('APP_PORT', '80')
    HOST = os.getenv('APP_HOST', '0.0.0.0')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=os.getenv('POSTGRES_USER', 'andriim'),
                                                                           pw=os.getenv('POSTGRES_PW', 'password'),
                                                                           url=os.getenv('POSTGRES_URL', '10.188.176.3:5432'),
                                                                           db=os.getenv('POSTGRES_DB', 'lab4db'))
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
