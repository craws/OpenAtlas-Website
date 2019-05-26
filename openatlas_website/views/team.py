# Created by Alexander Watzinger and others. Please see README.md for licensing information
from collections import OrderedDict

from flask import render_template

from openatlas_website import app


@app.route('/team')
def team():
    team_ = OrderedDict([
        ('Stefan Eichert', {
            'email': 'stefan.eichert@oeaw.ac.at',
            'function': 'Idea, Concept and Data Modelling',
            'img': 'stefan.jpg',
            'image_license': ''}),
        ('Alexander Watzinger', {
            'email': 'alexander.watzinger@oeaw.ac.at',
            'function': 'Software Development and Concept',
            'img': 'alex.png',
            'image_license': 'CC-BY 4.0, Jan Belik'}),
        ('Jan Belik', {
            'email': 'buero@janbelik.com',
            'function': 'Logo and Design Consulting',
            'img': 'jan.png',
            'image_license': 'CC-BY 4.0, Jan Belik'}),
        ('Daniel Kittel', {
            'email': 'daniel.kittel@craws.net',
            'function': 'Quality Assurance',
            'img': 'daniel.png',
            'image_license': 'CC-BY 4.0, Jan Belik'}),
        ('Christoph Hoffmann', {
            'email': 'christoph.hoffmann@oeaw.ac.at',
            'function': 'Frontend Development',
            'img': 'christoph.jpg',
            'image_license': 'CC-BY 4.0, Sandra Lehecka'}),
        ('Bernhard Koschicek', {
            'email': 'bernhard.koschicek@oeaw.ac.at',
            'function': 'Software Development',
            'img': 'bernhard.jpg',
            'image_license': ''})])
    return render_template('team.html', team=team_)
