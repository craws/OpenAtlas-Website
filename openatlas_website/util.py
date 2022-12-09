from typing import Iterator

from flask import url_for

from openatlas_website import app
from openatlas_website.data.institute import institutes
from openatlas_website.data.team import team


@app.template_filter()
def display_menu(route: str) -> str:
    html = ''
    for item in [
            'about', 'projects', 'cooperation', 'software', 'team', 'events']:
        active = 'active' if route.startswith('/' + item) \
            or item == 'about' and route in ['/', '/news'] else ''
        html += \
            f'<li class="nav-item">' \
            f'<a class="nav-link {active}" href="{url_for(item)}">' \
            f'{item.upper()}</a></li>'
    return html


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
    return f'<div>{html}</div>'


@app.template_filter()
def display_team_member(name: str) -> str:
    person = team[name]
    html = f"""
    <div class="row">
    <div class="col-md-auto mb-4">
        <img class="team" src="/static/images/team/{person['img']}" alt="">
        <br>"""
    if person['image_license']:
        html += f'<span class="image-license">{person["image_license"]}</span>'
    return html + f"""
        </div>
        <div class="col">
            <p>
                <span style="font-weight: bold;">{name}</span><br>
                {person['function']}<br>
                <a href="mailto:{['person.email']}">{person['email']}</a>
            </p>
            <p>{person['text']}</p>
      </div></div>"""
