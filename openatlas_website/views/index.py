# Created by Alexander Watzinger and others. Please see README.md for licensing information
from flask import render_template

from openatlas_website import app


@app.route('/')
def about() -> str:
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e), 404
