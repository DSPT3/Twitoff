""" Code for our App """

from flask import Flask

# Make app factory

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def root():
        return 'Welcome to Twitoff!!!'
    return app
