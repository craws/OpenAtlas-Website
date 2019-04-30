# Created by Alexander Watzinger and others. Please see README.md for licensing information
import re

import flask
import jinja2
from flask_babel import format_number as babel_format_number
from jinja2 import escape, evalcontextfilter

from openatlas_website.util import util

blueprint = flask.Blueprint('filters', __name__)
paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')


@jinja2.contextfilter
@blueprint.app_template_filter()
def format_number(self, number):
    return babel_format_number(number)


@jinja2.contextfilter
@blueprint.app_template_filter()
def uc_first(self, string):
    return util.uc_first(string)


@jinja2.contextfilter
@blueprint.app_template_filter()
@evalcontextfilter
def nl2br(self, value):
    result = u'\n\n'.join(
        u'<p>%s</p>' % p.replace('\n', '<br>\n') for p in paragraph_re.split(escape(value)))
    return result
