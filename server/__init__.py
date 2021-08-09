from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "data.db"

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='12ws34rfvZNsuper_secret_lolyv%ybu$&#fFG',
            SQLALCHEMY_DATABASE_URI='sqlite:///data.db',
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            DEBUG=True
    )

    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    create_database(app)

    return app

def create_database(app):
    db.create_all(app=app)
    print('>> Database Initialized <<')

