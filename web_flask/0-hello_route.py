#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

# Create a Flask web app
@app.route('/', strict_slashes=False)
def hello():
    """
    Returns a greeting message.

    This function returns a plain text greeting message, 'Hello HBNB!',
    which can be used to greet users or provide a simple welcome.

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
