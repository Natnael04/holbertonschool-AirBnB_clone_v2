#!/usr/bin/python3

"""Create a Flask web app.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def about():
    return 'HBNB'


@app.route('/c/hi', strict_slashes=False)
def index():
    text_variable = "C"
    return (text_variable)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
