# Created by Alexander Watzinger and others. Please see README.md for licensing information
from typing import Iterator

import flask
from flask import request, url_for

from openatlas_website.util import util

blueprint = flask.Blueprint('filters', __name__)

INSTITUTES = {
    'OEAW': {
        'name': 'Austrian Academy of Sciences',
        'url': 'https://www.oeaw.ac.at/',
        'logo': 'oeaw.png'},
    'IMAFO': {
        'name': 'Institute for Medieval Research',
        'url': 'https://www.oeaw.ac.at/imafo/',
        'logo': 'imafo.png'},
    'ACDH': {
        'name': 'Austrian Centre for Digital Humanities',
        'url': 'https://www.oeaw.ac.at/acdh/',
        'logo': 'acdh.png'},
    'ERC': {
        'name': 'European Research Council',
        'url': 'https://erc.europa.eu/',
        'logo': 'erc.png'},
    'univie': {
        'name': 'University of Vienna',
        'url': 'https://www.univie.ac.at/',
        'logo': 'uni_vienna.jpg'},
    'FWF': {
        'name': 'Austrian Science Fund',
        'url': 'https://www.fwf.ac.at/',
        'logo': 'fwf.png'},
    'OeAI': {
        'name': 'Austrian Archaeological Institute',
        'url': 'https://www.oeaw.ac.at/oeai/',
        'logo': 'oeai.png'},
    'RHUL': {
        'name': 'Royal Holloway University of London',
        'url': 'https://www.royalholloway.ac.uk/',
        'logo': 'rhul.png'},
    'MU': {
        'name': 'Masaryk University ',
        'url': 'https://www.muni.cz/',
        'logo': 'mu.png'},
    'GACR': {
        'name': 'Czech Science Foundation ',
        'url': 'https://gacr.cz',
        'logo': 'gacr.png'}}


@blueprint.app_template_filter()
def display_menu(unused_variable) -> str:
    """ Returns HTML with the menu and mark appropriate item as selected."""
    html = ''
    selected = ''
    items = ['about', 'projects', 'team', 'events']
    for item in items:
        if selected:  # pragma: no cover
            active = 'active' if item == selected else ''
        else:
            active = 'active' if request.path.startswith('/' + item) or \
                                 (item == 'about' and request.path == '/') else ''
        html += '<a class="nav-item nav-link {active}" href="{url}">{label}</a>'.format(
            active=active, url=url_for(item), label=item.upper())
    return html


@blueprint.app_template_filter()
def display_institutes(institutes: Iterator) -> str:
    html = ''
    for short_name in institutes:
        institute = INSTITUTES[short_name]
        html += '''
            <a href="{url}" target="_blank" class="img">
                <img src="/static/images/credits/{logo}" alt="{name}" title="{name}"/>
            </a>'''.format(url=institute['url'], logo=institute['logo'], name=institute['name'])
    return html
