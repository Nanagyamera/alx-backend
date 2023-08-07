#!/usr/bin/env python3
"""
A Basic Flask app.
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


# Config class with LANGUAGES class attribute
class Config:
    """
    Represents the Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instantiate Babel object and set app config
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    """
    This is the home page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
