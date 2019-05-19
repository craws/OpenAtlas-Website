# Created by Alexander Watzinger and others. Please see README.md for licensing information
import flask
import jinja2
from flask import request, url_for

from openatlas_website.util import util

blueprint = flask.Blueprint('filters', __name__)

@jinja2.contextfilter
@blueprint.app_template_filter()
def display_menu(self, origin):
    """ Returns HTML with the menu and mark appropriate item as selected."""
    html = ''
    selected = origin.view_name if origin else ''
    items = ['about', 'projects', 'team']
    for item in items:
        if selected:
            active = 'active' if item == selected else ''
        else:
            active = 'active' if request.path.startswith('/' + item) or \
                              (item == 'about' and request.path == '/') else ''
        html += '<a class="nav-item nav-link {active}" href="{url}">{label}</a>'.format(
                active=active, url=url_for(item), label=util.uc_first(item))
    return html
