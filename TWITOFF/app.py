""" Code for our App """

from decouple import config
from flask import Flask, render_template, request
from .models import DB, User

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
        users = User.query.all()
        return render_template('base.html', title = 'Home', users=users)
    return app
