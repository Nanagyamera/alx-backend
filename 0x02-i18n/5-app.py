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


@app.route('/')
def index() -> str:
    """
    This is the home page
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
