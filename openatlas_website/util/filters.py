# Created by Alexander Watzinger and others. Please see README.md for licensing information
import re

import flask
import jinja2
from flask import request, url_for
from flask_babel import format_number as babel_format_number, lazy_gettext as _
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


@jinja2.contextfilter
@blueprint.app_template_filter()
def display_menu(self, origin):
    """ Returns html with the menu and mark appropriate item as selected."""
    html = ''
    selected = origin.view_name if origin else ''
    items = ['about', 'screenshots', 'team', 'history']
    for item in items:
        if selected:
            active = 'active' if item == selected else ''
        else:
            active = 'active' if request.path.startswith('/' + item) or \
                              (item == 'about' and request.path == '/') else ''
        html += '<a class="nav-item nav-link {active}" href="{url}">{label}</a>'.format(
                active=active, url=url_for(item), label=util.uc_first(_(item)))
    return html
