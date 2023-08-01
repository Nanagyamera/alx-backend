#!/usr/bin/env python3
"""
A Basic Flask app with internationalization support.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)


# Config class with LANGUAGES class attribute
class Config:
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
    Check if 'locale' is present in the request args and is a supported locale
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

# Resort to the default behavior
    supported_languages = app.config['LANGUAGES']
    return request.accept_languages.best_match(supported_languages)


@app.route('/')
def index() -> str:
    """
    This is the home page
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
