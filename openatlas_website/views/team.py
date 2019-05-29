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
            'text': '',
            'img': 'stefan.jpg',
            'image_license': ''}),
        ('Alexander Watzinger', {
            'email': 'alexander.watzinger@oeaw.ac.at',
            'function': 'Software Development and Concept',
            'text': '''Alex
                    is a software developer with a special interest in data modeling and scientific                    
                    'web applications. In the last few years, he has acted as the main developer of 
                    OpenAtlas, an open source database application that enables users to manage 
                    complex historical, archeological, and geospatial data.''',
            'img': 'alex.png',
            'image_license': 'CC-BY 4.0, Jan Belik'}),
        ('Jan Belik', {
            'email': 'buero@janbelik.com',
            'function': 'Logo Design and Design Consulting',
            'text': '''Jan is a freelance Graphic Designer, Illustrator and Art Director at 
                        <a href="https://janbelik.com" target="_blank">janbelik.com</a> in Vienna, 
                        Austria. 
                        He has plenty of experience working with local and 
                        international brands and has created a range of OpenAtlas project logos.''',
            'img': 'jan.png',
            'image_license': 'CC-BY 4.0, Jan Belik'}),
        ('Daniel Kittel', {
            'email': 'daniel.kittel@craws.net',
            'function': 'Quality Assurance',
            'text': '',
            'img': 'daniel.png',
            'image_license': 'CC-BY 4.0, Jan Belik'}),
        ('Christoph Hoffmann', {
            'email': 'christoph.hoffmann@oeaw.ac.at',
            'function': 'Frontend Development',
            'text': '''Christoph completed his education as a librarian in 2014 at the Library of 
                        the University of Vienna. After working as a systems librarian at the 
                        Austrian National Library and as a cataloger for the Austrian Workers 
                        Chamber, he joined the ACDH Team in 2015 as a manager of archival software. 
                        He is also engaged in Webdesign and Frontend-Development. As a philosophy 
                        student at the University of Vienna, he is interested in the epistemological 
                        implications of digital research methods in the humanities.''',
            'img': 'christoph.jpg',
            'image_license': 'CC-BY 4.0, Sandra Lehecka'}),
        ('Bernhard Koschicek', {
            'email': 'bernhard.koschicek@oeaw.ac.at',
            'function': 'Software Development',
            'text': '''Berni is a student of Computer Sciences at the University of Applied Sciences 
                        Technikum Wien and currently student of history at University of Vienna. 
                        Research interests include computer security, python, digital reservation, 
                        historical geographie, GIS, medieval and military history.''',
            'img': 'bernhard.jpg',
            'image_license': ''})])
    return render_template('team.html', team=team_)
