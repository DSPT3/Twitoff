""" Code for our App """

from flask import Flask
from .models import DB

# Make app factory

def create_app():
    app = Flask(__name__)

    # Add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Have the database know about the app
    DB.init_app(app)
    
    @app.route("/")
    def root():
        return 'Welcome to Twitoff!!!'
    return app
