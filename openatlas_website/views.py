from typing import Dict, Tuple

from flask import render_template

from openatlas_website import app
from openatlas_website.data.contributors import get_contributor_lists
from openatlas_website.data.event import past, upcoming
from openatlas_website.data.news import news_
from openatlas_website.data.project import projectList
from openatlas_website.data.software import stack
from openatlas_website.filters import sanitize


@app.route('/')
def about() -> str:
    return render_template(
        'about.html',
        latest_news_item=next(iter(news_['News'].values())))


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
    tags: Dict[str, int] = {}
    for project in projectList.values():
        # Assuming an existing 'urls' dict we extract the first as 'main_url'
        project['main_url'] = project['url']
        project['tags_sanitized'] = []
        for tag in project['tags']:
            sanitized_tag = sanitize(tag)
            project['tags_sanitized'].append(sanitized_tag)

            # Add to tags dictionary (count occurrences)
            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1

    # Create sanitized HTML items for unique tags
    unique_tag_items = [
        f'<div id="{sanitize(tag)}">{tag}</div>' for tag in sorted(tags)]

    return render_template(
        'projects.html',
        projectList=projectList,
        unique_tags=f'<div id="tags">{"".join(unique_tag_items)}</div>')


@app.route('/software')
def software() -> str:
    return render_template('software.html', stack=stack)


@app.route('/team')
def team() -> str:
    return render_template('team.html', contributors=get_contributor_lists())


@app.route('/mission')
def mission_statement() -> str:
    return render_template('mission.html')
