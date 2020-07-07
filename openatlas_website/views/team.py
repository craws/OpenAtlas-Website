from collections import OrderedDict

from flask import render_template

from openatlas_website import app


@app.route('/team')
def team() -> str:
    team_ = OrderedDict([
        ('Stefan Eichert', {
            'email': 'stefan.eichert@univie.ac.at',
            'function': 'Idea, Concept and Data Modelling',
            'text': """Stefan is the the initiator and master mind behind the OpenAtlas project.
                His main research fields are early medieval history and archaeology as well as
                computer applications in archaeology and digital humanities.""",
            'img': 'stefan.jpg',
            'image_license': 'CC-BY 4.0,<br> Sandra Lehecka'}),
        ('Alexander Watzinger', {
            'email': 'alexander.watzinger@oeaw.ac.at',
            'function': 'Lead Developer and Concept',
            'text': """Alex is the lead developer of OpenAtlas and has a special interest
                in data modeling and scientific web applications. His favorite tools are Python,
                PostgreSQL, Linux, and open source software in general.""",
            'img': 'alex.jpg',
            'image_license': 'CC-BY 4.0,<br> Sandra Lehecka'}),
        ('Bernhard Koschicek', {
            'email': 'bernhard.koschicek@oeaw.ac.at',
            'function': 'Software Development',
            'text': """Berni is a student of Computer Sciences and currently student of history.
            Research interests include computer security, Python, digital reservation,
            historical geographie, GIS, medieval and military history.""",
            'img': 'bernhard.jpg',
            'image_license': 'CC-BY 4.0,<br> Sandra Lehecka'}),
        ('Christoph Hoffmann', {
            'email': 'christoph.hoffmann@oeaw.ac.at',
            'function': 'Frontend Development',
            'text': """Christoph is engaged in web design and frontend development. As a philosophy
            student at the University of Vienna, he is interested in the epistemological
            implications of digital research methods in the humanities.""",
            'img': 'christoph.jpg',
            'image_license': 'CC-BY 4.0,<br> Sandra Lehecka'}),
        ('Veronika Gründhammer', {
            'email': 'veronika.gruendhammer@oeaw.ac.at',
            'function': 'Project Administration',
            'text': """Veronika provides essential support for cooperations in her role as project officer at the
                <a target="_blank" href='https://www.oeaw.ac.at/acdh/'>ACDH-CH</a>.""",
            'img': 'veronika.jpg',
            'image_license': ''}),
        ('Jan Belik', {
            'email': 'buero@janbelik.com',
            'function': 'Logo Design and Design Consulting',
            'text': """Jan is a freelance Graphic Designer, Illustrator and Art Director at
                <a href="https://janbelik.com" target="_blank">janbelik.com</a> in Vienna, Austria.
                He has plenty of experience working with local and international brands and has
                created a range of OpenAtlas project logos.""",
            'img': 'jan.jpg',
            'image_license': 'CC-BY 4.0,<br> Sandra Lehecka'}),
        ('Nina Brundke', {
            'email': 'nina.brundke@oeai.at',
            'function': 'Bioarchaeological Expertise',
            'text': """Nina studied medieval and modern archaeology at the Otto-Friedrich University, 
                Bamberg, and studied biology with a concentration on anthropology at the University of Vienna. 
                With her expertise she provides essential support planning and implementing archeological 
                modules in OpenAtlas.""",
            'img': 'nina.jpg',
            'image_license': 'CC-BY 4.0,<br> Jan Belik'})
    ])
    return render_template('team.html', team=team_)
