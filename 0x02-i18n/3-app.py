#!/usr/bin/env python3
"""A module that contains Flask app"""


from flask import Flask, render_template, request
from flask_babel import Babel

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
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """A function that defines the best match for locale languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    """this is main function"""
    app.run(host='0.0.0.0', port=5000, debug=True)
