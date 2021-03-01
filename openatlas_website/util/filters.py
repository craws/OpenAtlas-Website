from typing import Any, Iterator

import flask
import jinja2
from flask import url_for

from openatlas_website.data.institute import INSTITUTES

blueprint: flask.Blueprint = flask.Blueprint('filters', __name__)


@jinja2.contextfilter
@blueprint.app_template_filter()
def display_menu(self: Any, route: str) -> str:
    """ Returns HTML with the menu and mark appropriate item as selected."""
    html = ''
    items = ['about', 'projects', 'features', 'software', 'team', 'events']
    for item in items:
        active = ''
        if route.startswith('/' + item):
            active = 'active'
        if item == 'about' and route in ['/', '/cooperation', '/cooperation/information']:
            active = 'active'
        html += '<a class="nav-item nav-link {active}" href="{url}">{label}</a>'.format(
            active=active, url=url_for(item), label=item.upper())
    return html


@jinja2.contextfilter
@blueprint.app_template_filter()
def display_institutes(self: Any, institutes: Iterator) -> str:
    html = '<div>'
    for short_name in institutes:
        institute = INSTITUTES[short_name]
        html += '''
            <a href="{url}" target="_blank" class="without-decoration">
                <img src="/static/images/institutes/{logo}" alt="{name}" title="{name}">
            </a>'''.format(url=institute['url'], logo=institute['logo'], name=institute['name'])
    return html + '</div>'
