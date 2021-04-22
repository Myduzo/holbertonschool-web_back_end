#!/usr/bin/env python3
""" Basic Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """ Babel config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """ GET /
        return render_template
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """ Get locale that returns
    the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
