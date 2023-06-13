#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel, request

app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def Welcome():
    """basic Flask app"""
    return render_template('4-index.html')


class Config(object):
    """Supported languages list"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """function with the babel.localeselector decorator.
    Use request.accept_languages to determine the best
    match with our supported languages"""
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])