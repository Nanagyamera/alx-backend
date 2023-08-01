#!/usr/bin/env python3
"""
A Basic Flask app with internationalization support.
"""
from flask import Flask, render_template, request, g
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

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# Define the get_user function
def get_user(user_id) -> Union[Dict, None]:
    """
    Retrieves a user based on a user id.
    """
    return users.get(user_id)


# Define the before_request function
@app.before_request
def before_request():
    """
    Performs certain routines before each request's resolution.
    """
    login_as = request.args.get('login_as')
    if login_as is not None:
        user_id = int(login_as)
        g.user = get_user(user_id)
    else:
        g.user = None


# Define the get_locale function with updated priority
@babel.localeselector
def get_locale() -> str:
    """
    Check if the locale is provided in the URL parameters
    """
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    # Check if a user is logged in and their locale is supported
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Use the locale from the request header
    header_locale = request.accept_languages.best_match(
        app.config['LANGUAGES']
    )
    if header_locale:
        return header_locale

    # Resort to the default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
