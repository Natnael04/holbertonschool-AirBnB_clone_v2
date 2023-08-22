#!/usr/bin/python3

"""Create a Flask web app.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C %s" % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    formatted_text = text.replace("_", " ")
    return "Python " + formatted_text


@app.route('/number/<int:n>', strict_slashes=False)
def check_n(n):
    if isinstance(n, int):
        return 'n is a number.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
