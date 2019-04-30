# Created by Alexander Watzinger and others. Please see README.md for licensing information
from flask import render_template

from openatlas_website import app


@app.route('/')
def index():
    return render_template('index.html', intro='This is the intro')
