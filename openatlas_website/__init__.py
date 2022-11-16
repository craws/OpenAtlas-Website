from pathlib import Path
from flask import Flask, Response, request

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

if (Path(app.root_path).parent / 'instance' / 'production.py').is_file():
    app.config.from_pyfile('production.py')

# pylint: disable=wrong-import-position, import-outside-toplevel
from openatlas_website import util, views


@app.before_request
def before_request() -> None:
    if request.path.startswith('/static'):
        return  # Only needed if not running with apache and static alias


@app.after_request
def apply_caching(response: Response) -> Response:
    response.headers['Strict-Transport-Security'] = \
        'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
