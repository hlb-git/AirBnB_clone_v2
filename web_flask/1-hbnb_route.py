#!/usr/bin/python3
"""Web flask application"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """The landing page that returns “Hello HBNB!”"""
    
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""

    return "HBNB"

if __name__ == "__main__":
    app.run()
