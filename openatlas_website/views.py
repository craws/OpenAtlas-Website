from typing import Tuple

from flask import render_template

from openatlas_website import app
from openatlas_website.data.event import past, upcoming
from openatlas_website.data.news import news_
from openatlas_website.data.project import concluded, current
from openatlas_website.data.software import stack


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
    return render_template('projects.html', current=current, past=concluded)

@app.route('/software')
def software() -> str:
    return render_template('software.html', stack=stack)

@app.route('/team')
def team() -> str:
    return render_template('team.html')
