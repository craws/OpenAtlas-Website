# Created by Alexander Watzinger and others. Please see README.md for licensing information
import locale
import os

from flask import Flask, request, session
from flask_babel import Babel
from flask_wtf.csrf import CsrfProtect

try:
    import mod_wsgi
except ImportError:
    mod_wsgi = None

app = Flask(__name__, instance_relative_config=True)
csrf = CsrfProtect(app)  # Make sure all forms are CSRF protected

# Use the test database if running tests
app.config.from_object('config.default')  # Load config
app.config.from_pyfile('production.py')  # Load instance

if os.name == "posix":  # For other operating systems e.g. Windows, we would need adaptions here
    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')  # pragma: no cover

babel = Babel(app)

from openatlas_website.util import filters
from openatlas_website.views import index


@babel.localeselector
def get_locale():
    if 'language' in session:
        return session['language']
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'].keys())
    # Check if best_match is set (in tests it isn't)
    return best_match if best_match else 'en'


@app.before_request
def before_request():
    if request.path.startswith('/static'):  # pragma: no cover
        return  # Only needed if not running with apache and static alias
    session['language'] = get_locale()


@app.after_request
def apply_caching(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'

    # Todo: activate Content-Security-Policy after removal of every inline CSS and JavaScript
    # response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response


app.register_blueprint(filters.blueprint)


if __name__ == "__main__":  # pragma: no cover
    app.run()
