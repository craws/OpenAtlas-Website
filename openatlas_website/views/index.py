# Created by Alexander Watzinger and others. Please see README.md for licensing information
from flask import render_template

from openatlas_website import app


@app.route('/')
def about():
    return render_template('about.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html', e=e), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e), 404


@app.errorhandler(418)
def invalid_id(e):
    return render_template('418.html', e=e), 418
