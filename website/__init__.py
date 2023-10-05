from flask import Flask, Blueprint, render_template, request, session, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from os import path
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    print(__name__)
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jesusislord'

    # Set app configuration data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    db.init_app(app)

    from website.views import mainbp
    from website.auth import authenticationbp
    app.register_blueprint(mainbp)
    app.register_blueprint(authenticationbp)

    # Initialise bootstrap
    bootstrap = Bootstrap(app)

    from .models import Events

    with app.app_context():
        db.create_all()


    return app

