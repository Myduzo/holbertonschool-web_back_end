#!/usr/bin/env python3
""" Basic Babel setup
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ Get locale that returns
    the best match with our supported languages
    - Force locale with URL parameter -
    """
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    id = request.args.get('login_as')
    user = get_user(id)
    if user:
        g.user = user


def get_user(id):
    if id and int(id) in users:
        return users.get(id)

    return None


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
