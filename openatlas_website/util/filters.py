from typing import Any, Iterator

import flask
import jinja2
from flask import url_for

blueprint: flask.Blueprint = flask.Blueprint('filters', __name__)

INSTITUTES = {
    'ACDH': {
        'name': 'Austrian Centre for Digital Humanities and Cultural Heritage',
        'url': 'https://www.oeaw.ac.at/acdh/',
        'logo': 'acdh.png'},
    'AIT': {
        'name': 'Austrian Institute of Technology',
        'url': 'https://www.ait.ac.at/',
        'logo': 'ait.jpg'},
    'ARUP': {
        'name': 'Institute of archaeology of the CAS',
        'url': 'https://www.arup.cas.cz/',
        'logo': 'arup.jpg'},
    'BCM': {
        'name': 'Belgrade City Museum',
        'url': 'http://www.mgb.org.rs/en/',
        'logo': 'bcm.png'},
    'Biblioteka Matice Srpske': {
        'name': 'Biblioteka Matice Srpske',
        'url': 'http://www.bms.ns.ac.rs/bms101.htm',
        'logo': 'biblioteka_matice_srpske.png'},
    'Byzantine Research': {
        'name': 'Byzantine Research',
        'url': 'https://www.oeaw.ac.at/en/byzantine-research/',
        'logo': 'byzantine_research.jpg'},
    'ELTE': {
        'name': 'Eötvös Loránd University',
        'url': 'https://www.elte.hu/',
        'logo': 'elte.svg'},
    'ERC': {
        'name': 'European Research Council',
        'url': 'https://erc.europa.eu/',
        'logo': 'erc.png'},
    'FWF': {
        'name': 'Austrian Science Fund',
        'url': 'https://www.fwf.ac.at/',
        'logo': 'fwf.png'},
    'GACR': {
        'name': 'Czech Science Foundation ',
        'url': 'https://gacr.cz',
        'logo': 'gacr.png'},
    'IAS': {
        'name': 'Institute for Advanced Study',
        'url': 'https://www.ias.edu/',
        'logo': 'ias.svg'},
    'IMAFO': {
        'name': 'Institute for Medieval Research',
        'url': 'https://www.oeaw.ac.at/imafo/',
        'logo': 'imafo.png'},
    'JGU': {
        'name': 'Johannes Gutenberg University Mainz',
        'url': 'https://www.uni-mainz.de/eng/index.php',
        'logo': 'jug.png'},
    'MPI-SHH': {
        'name': 'Max Planck Institute for the Science of Human History',
        'url': 'https://www.shh.mpg.de/',
        'logo': 'mpi-ssh.png'},
    'MSMT': {
        'name': 'Ministry of Education, Youth and Sports',
        'url': 'https://www.msmt.cz',
        'logo': 'msmt.png'},
    'MU': {
        'name': 'Masaryk University ',
        'url': 'https://www.muni.cz/',
        'logo': 'mu.png'},
    'NHM': {
        'name': 'Natural History Museum Vienna',
        'url': 'https://www.nhm-wien.ac.at/',
        'logo': 'nhm.svg'},
    'NLS': {
        'name': 'National Library of Serbia',
        'url': 'https://www.nb.rs',
        'logo': 'nls.jpg'},
    'OeAI': {
        'name': 'Austrian Archaeological Institute',
        'url': 'https://www.oeaw.ac.at/oeai/',
        'logo': 'oeai.png'},
    'OEAW': {
        'name': 'Austrian Academy of Sciences',
        'url': 'https://www.oeaw.ac.at/',
        'logo': 'oeaw.png'},
    'RHUL': {
        'name': 'Royal Holloway University of London',
        'url': 'https://www.royalholloway.ac.uk/',
        'logo': 'rhul.png'},
    'TIB': {
        'name': 'Tabula Imperii Byzantini',
        'url': 'https://tib.oeaw.ac.at',
        'logo': 'tib.png'},
    'UAI': {
        'name': 'Union Académique Internationale',
        'url': 'http://www.uai-iua.org/en',
        'logo': 'uai.jpg'},
    'univie': {
        'name': 'University of Vienna',
        'url': 'https://www.univie.ac.at/',
        'logo': 'uni_vienna.jpg'},
    'Wien Kultur': {
        'name': 'Wien Kultur (MA 7)',
        'url': 'https://www.wien.gv.at/kultur/abteilung/',
        'logo': 'wien_kultur.jpg'}
}


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
            <a href="{url}" target="_blank">
                <img src="/static/images/institutes/{logo}" alt="{name}" title="{name}">
            </a>'''.format(url=institute['url'], logo=institute['logo'], name=institute['name'])
    return html + '</div>'
