# Created by Alexander Watzinger and others. Please see README.md for licensing information
from typing import Iterator

import flask
import jinja2
from flask import request, url_for

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


@jinja2.contextfilter
@blueprint.app_template_filter()
def display_menu(self, unused_variable) -> str:
    """ Returns HTML with the menu and mark appropriate item as selected."""
    html = ''
    items = ['about', 'projects', 'team', 'events']
    for item in items:
        active = ''
        if request.path.startswith('/' + item):
            active = 'active'
        if item == 'about' and request.path == '/':
            active = 'active'
        html += '<a class="nav-item nav-link {active}" href="{url}">{label}</a>'.format(
            active=active, url=url_for(item), label=item.upper())
    return html


@jinja2.contextfilter
@blueprint.app_template_filter()
def display_institutes(self, institutes: Iterator) -> str:
    html = ''
    for short_name in institutes:
        institute = INSTITUTES[short_name]
        html += '''
            <a href="{url}" target="_blank" class="img">
                <img src="/static/images/credits/{logo}" alt="{name}" title="{name}"/>
            </a>'''.format(url=institute['url'], logo=institute['logo'], name=institute['name'])
    return html
