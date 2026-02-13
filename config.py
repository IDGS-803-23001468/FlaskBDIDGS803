from sqlachemy import create_engins

class Config(object):
    SECRET_KEY:"ClaveSecreta"
    SESSION_COOKIE_SECURE=False
    
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Banquito02'