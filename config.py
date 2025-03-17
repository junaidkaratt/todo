import os

class myconfig:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+pymysql://junaid:password%40123@localhost/todo")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

