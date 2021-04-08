from typing import Iterator

from flask import url_for
from markupsafe import Markup

from openatlas_website import app
from openatlas_website.data.institute import institutes


@app.template_filter()
def display_menu(route: str) -> str:
    html = ''
    items = ['about', 'projects', 'features', 'software', 'team', 'events']
    for item in items:
        active = 'active' if route.startswith('/' + item) else ''
        if item == 'about' and route in ['/', '/cooperation', '/cooperation/information', '/news']:
            active = 'active'
        html += '''
            <li class="nav-item">
                <a class="nav-link {active}" href="{url}">{label}</a>
            </li>'''.format(active=active, url=url_for(item), label=item.upper())
    return Markup(html)


@app.template_filter()
def display_institutes(institutes_: Iterator) -> str:
    html = ''
    for short_name in institutes_:
        institute = institutes[short_name]
        html += '''
            <a href="{url}" target="_blank" class="without-decoration">
                <img src="/static/images/institutes/{logo}" alt="{name}" title="{name}">
            </a>'''.format(url=institute['url'], logo=institute['logo'], name=institute['name'])
    return Markup('<div>{html}</div>'.format(html=html))
