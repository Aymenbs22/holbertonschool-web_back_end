#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)



@app.route('/')
def Welcome():
    """basic Flask app"""
    return render_template('0-index.html')


class Config(object):
    """Supported languages list"""
    LANGUAGES = ['en', 'fr']


app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)