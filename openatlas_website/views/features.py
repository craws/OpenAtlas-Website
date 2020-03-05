from collections import OrderedDict

from flask import render_template

from openatlas_website import app


@app.route('/features')
def features() -> str:
    return render_template('features.html')
