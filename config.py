import os

class Config:
    """
    This is the parent class which will have the general configurations
    """
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    SECRET_KEY = 'samkasyoki'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://chris:blackpool005@localhost/crimmzpitch'

    #email stuff
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "ckaringe@gmail.com"
    MAIL_PASSWORD  = "blackpool006"

class DevConfig(Config):
    """
    This is the class which we will use to set the configurations during development stage of the app
    Args:
        Config - this is the parent config class from which we inherit its properties
    """

    DEBUG = True
    ENV = 'development'


class ProdConfig(Config):
    """
    This is the class which we will use to set the configurations during production stage of the app
    Args:
        Config - this is the parent config class from which we inherit its properties
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    """
    This is the class which we will use to set the configurations during testing stage of the app
    Args:
        Config - this is the parent config class from which we inherit its properties
    """


config_options = {
    "test": TestConfig,
    "production": ProdConfig,
    "development": DevConfig
}