from typing import Iterator

from flask import url_for
from markupsafe import Markup

from openatlas_website import app
from openatlas_website.data.institute import institutes


@app.template_filter()
def display_menu(route: str) -> str:
    html = ''
    for item in [
            'about', 'projects', 'features', 'software', 'team', 'events']:
        active = 'active' if route.startswith('/' + item) else ''
        if item == 'about' and route \
                in ['/', '/cooperation', '/cooperation/information', '/news']:
            active = 'active'
        html += f"""
            <li class="nav-item">
                <a class="nav-link {active}" href="{url_for(item)}"
                    >{item.upper()}</a>
            </li>"""
    return Markup(html)


@app.template_filter()
def display_institutes(institutes_: Iterator[str]) -> str:
    html = ''
    for name in institutes_:
        html += f"""
            <a
                href="{institutes[name]['url']}"
                target="_blank"
                class="without-decoration">
                <img
                    src="/static/images/institutes/{institutes[name]['logo']}"
                    alt="{institutes[name]['name']}"
                    title="{institutes[name]['name']}">
            </a>"""
    return Markup(f'<div>{html}</div>')
