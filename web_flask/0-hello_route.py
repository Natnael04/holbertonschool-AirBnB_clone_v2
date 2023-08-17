#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

# Create a Flask web app


@app.route('/', strict_slashes=False)
def hello():
    """
    A route function that returns a simple greeting message.

    This function is associated with the root URL ('/'). When a user
    accesses the root URL, this function will be invoked, and it will
    return a plain text message saying "Hello, World!".

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """
    Entry point for running the Flask app.

    This block of code checks if the script is being run directly (as
    opposed to being imported as a module). If it's the main script,
    it starts the Flask development server, allowing the app to be
    accessed via a web browser.

    Note:
        The development server is only meant for testing purposes and
        should not be used in a production environment.

    Usage:
        Run this script directly using Python to start the Flask app.
    """
    app.run(host='0.0.0.0', port=5000)
