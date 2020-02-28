from typing import Any, Iterator

import flask
import jinja2
from flask import request, url_for

blueprint: flask.Blueprint = flask.Blueprint('filters', __name__)

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
        'name': 'Austrian Centre for Digital Humanities and Cultural Heritage',
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
        'logo': 'gacr.png'},
    'Wien Kultur': {
        'name': 'Wien Kultur (MA 7)',
        'url': 'https://www.wien.gv.at/kultur/abteilung/',
        'logo': 'wien_kultur.jpg'},
    'Byzantine Research': {
        'name': 'Byzantine Research',
        'url': 'https://www.oeaw.ac.at/en/byzantine-research/',
        'logo': 'byzantine_research.jpg'},
    'AIT': {
        'name': 'Austrian Institute of Technology',
        'url': 'https://www.ait.ac.at/',
        'logo': 'ait.jpg'},
    'BCM': {
        'name': 'Belgrade City Museum',
        'url': 'http://www.mgb.org.rs/en/',
        'logo': 'bcm.png'},
    'NLS': {
        'name': 'National Library of Serbia',
        'url': 'https://www.nb.rs',
        'logo': 'nls.jpg'},
    'Biblioteka Matice Srpske': {
        'name': 'Biblioteka Matice Srpske',
        'url': 'http://www.bms.ns.ac.rs/bms101.htm',
        'logo': 'biblioteka_matice_srpske.png'},
    'TIB': {
        'name': 'Tabula Imperii Byzantini',
        'url': 'https://tib.oeaw.ac.at',
        'logo': 'tib.png',},
    'UAI': {
        'name': 'Union Académique Internationale',
        'url': 'http://www.uai-iua.org/en',
        'logo': 'uai.jpg'},
    'MSMT': {
        'name': 'Ministry of Education, Youth and Sports',
        'url': 'http://www.msmt.cz',
        'logo': 'msmt.png'},
    'ARUP': {
        'name': 'Institute of archaeology of the CAS',
        'url': 'http://www.arup.cas.cz/',
        'logo': 'arup.jpg'},
}


@jinja2.contextfilter
@blueprint.app_template_filter()
def display_menu(self: Any, route: str) -> str:
    """ Returns HTML with the menu and mark appropriate item as selected."""
    html = ''
    items = ['about', 'projects', 'team', 'events']
    for item in items:
        active = ''
        if route.startswith('/' + item):
            active = 'active'
        if item == 'about' and route == '/':
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
            <a href="{url}" target="_blank">
                <img src="/static/images/institutes/{logo}" alt="{name}" title="{name}">
            </a>'''.format(url=institute['url'], logo=institute['logo'], name=institute['name'])
    html += '</div>'
    return html
