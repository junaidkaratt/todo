from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config.from_object('config.myconfig')

    db.init_app(app)
    Migrate(app,db)
    CORS(app)
    from app.routes import todo_bp
    app.register_blueprint(todo_bp)

    return app


