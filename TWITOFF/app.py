""" Code for our app """

from flask import Flask
from flask_migrate import Migrate
from .models import DB
# Make the app factory

def create_app():
    app = Flask(__name__)
    migrate = Migrate()

    # Add config for the database

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # Let the database know about the app

    DB.init_app(app)
    migrate.init_app(app, DB)

    #Routes

    @app.route('/')
    def root():
        return "Welcome to Twitoff!!!"
    return app
