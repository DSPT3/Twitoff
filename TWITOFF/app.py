""" Code for our app """

from flask import Flask

# Make the app factory

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return "Welcome to Twitoff!!!"
    return app
