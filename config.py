import os
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "mysql://root:" + SECRET_KEY + '@127.0.0.1/Movies'
    DEBUG = True
    CSRF_ENABLED = True
