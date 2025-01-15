from typing import Tuple

from flask import render_template

from openatlas_website import app
from openatlas_website.data.contributors import get_contributor_lists
from openatlas_website.data.event import past, upcoming
from openatlas_website.data.news import news_
from openatlas_website.data.project import projectList, tags
from openatlas_website.data.software import stack
from openatlas_website.filters import sanitize
from openatlas_website.data.publications import publicationsList


@app.route('/')
def about() -> str:
    return render_template(
        'about.html',
        latest_news=next(iter(news_['News'].items())))


@app.errorhandler(404)
def page_not_found(e: Exception) -> Tuple[str, int]:
    return render_template('404.html', e=e), 404


@app.route('/cooperation')
def cooperation() -> str:
    return render_template('cooperation.html')


@app.route('/cooperation/information')
def cooperation_information() -> str:
    return render_template('cooperation_information.html')


@app.route('/events')
def events() -> str:
    return render_template('events.html', past=past, upcoming=upcoming)


@app.route('/news')
def news() -> str:
    return render_template('news.html', news=news_)


@app.route('/projects')
def projects() -> str:
    for project in projectList.values():
        project['tags_sanitized'] = [sanitize(tag) for tag in project['tags']]
    return render_template(
        'projects.html',
        projectList=projectList,
        topic_tags=[
            f'<div id="{sanitize(t)}">{t}</div>' for t in tags['topic']],
        status_tags=[
            f'<div id="{sanitize(t)}">{t}</div>' for t in tags['status']])


@app.route('/publications')
def publications() -> str:
    return render_template('publications.html', publications=publicationsList)


@app.route('/software')
def software() -> str:
    return render_template('software.html', stack=stack)


@app.route('/team')
def team() -> str:
    return render_template('team.html', contributors=get_contributor_lists())


@app.route('/mission')
def mission_statement() -> str:
    return render_template('mission.html')
