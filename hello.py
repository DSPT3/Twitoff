""" Minimal Flask App """

from flask import Flask

# Make the application
app = Flask(__name__)

# Make the route
@app.route("/")

# Now define a function
def hello:
    return "Hello Twitoff...Again!"