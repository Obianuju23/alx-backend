#!/usr/bin/env python3
"""A module that contains Flask app"""


from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class that configures Babel app with instance attributes"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """function that returns html index for task 1"""
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """Function to determine the best match with our supported languages"""

    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    elif g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """ Returns the user dict if the ID is found """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
        else:
            return None


@app.before_request
def before_request():
    """ Finds a user and sets as the global on flask.g.user """
    g.user = get_user()


if __name__ == '__main__':
    """this is main function"""
    app.run(host='0.0.0.0', port=5000, debug=True)
