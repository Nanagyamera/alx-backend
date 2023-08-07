#!/usr/bin/env python3
"""
A Basic Flask app.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)


# Config class with LANGUAGES class attribute
class Config:
    """
    Represents the  Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instantiate Babel object and set app config
babel = Babel(app)
app.config.from_object(Config)


# get_locale function to determine the best match with supported languages
@babel.localeselector
def get_locale() -> str:
    """
    Retrieves the locale for a web page.
    """
    supported_languages = app.config['LANGUAGES']
    return request.accept_languages.best_match(supported_languages)


@app.route('/')
def index() -> str:
    """
    This is the home page
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
