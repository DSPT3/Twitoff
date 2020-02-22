""" Code for our app """

from decouple import config
from flask import Flask, render_template, request
from flask_migrate import Migrate
from .models import DB, User
# Make the app factory

def create_app():
    app = Flask(__name__)
    migrate = Migrate()

    # Add config for the database

    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    # stop tracking modifications on sqlalchemy config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Let the database know about the app

    DB.init_app(app)
    migrate.init_app(app, DB)

    #Routes

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title = 'Home', users=users)
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title = 'Reset', users=[])

    return app
