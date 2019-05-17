# Created by Alexander Watzinger and others. Please see README.md for licensing information
from collections import OrderedDict

from flask import render_template

from openatlas_website import app


@app.route('/')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    projects_ = OrderedDict([
        ('THANADOS', {
            'url': 'https://www.oeaw.ac.at/stipendien-foerderungen/foerderprogramme/godigital/godigital-next-generation-ausgewaehlte-projekte/',
            'full_name': 'The Anthropological and Archaeological Database of Sepultures',
            'img': '',
            'pi': 'Stefan Eichert',
            'duration': '2019 - 2022',
            'text': """hat zum Ziel ein Online Repositorium der frühmittelalterlichen Grabfunde
                Österreichs zu erschaffen. Es vereint mit Archäologie, Anthropologie und Digital
                Humanities drei Disziplinen. Die bisher bekannten und veröffentlichten Grabfunde
                werden dafür mit dem Open Source Datenbanksystem OpenAtlas, das die Informationen
                nach dem international etablierten Standard des CIDOC CRM modelliert,
                aufgenommen."""}),
        ('CONNEC', {
            'url': 'http://www.connectedclerics.com/',
            'full_name': 'Connected Clerics',
            'img': '/static/images/credits/logo_connec.png',
            'pi': 'David Natal',
            'duration': '2018 - 2022',
            'text': """analyses how a ‘universal’ late antique Church was constructed despite the 
                context of political fragmentation that precipitated the end of the Western 
                Roman Empire and its division into smaller polities."""}),
        ('DPP', {
            'url': 'http://dpp.oeaw.ac.at/',
            'full_name': 'Digitising Patterns of Power',
            'img': '/static/images/credits/logo_dpp.png',
            'pi': 'Mihailo Popović',
            'duration': '2015 - 2019',
            'text': """focuses on the analysis of the depiction of space in medieval written 
                sources, of the interaction between built and natural environment, of appropriation 
                of space and the emergence of new political, religious and economic structures of 
                power."""}),
        ('MEDCON', {
            'url': 'https://oeaw.academia.edu/MappingMedievalConflict',
            'full_name': 'Mapping Medieval Conflict',
            'img': '/static/images/credits/logo_medcon.png',
            'pi': 'Johannes Preiser-Kapeller',
            'duration': '2014 - 2017',
            'text': """examined the explanatory power of concepts of social and spatial network 
                    analysis for phenomena of political conflict in medieval societies."""}),
        ("Frontier, Contact Zone or No Man's Land", {
            'url': 'http://www.openatlas.eu/gkn',
            'full_name': "Frontier, Contact Zone or No Man's Land",
            'img': '/static/images/credits/logo_frontier.png',
            'pi': 'Stefan Eichert',
            'duration': '2012 - ???',
            'text': """ handelt um ein internationales österreichisch-tschechisches 
                Forschungsprojekt, das vom Österreichischen Wissenschaftsfond (FWF) und Grantová 
                agentura České republiky (GA ČR) gefördert wird."""}),
         ('The Eastern Alps Revisited', {
             'url': 'https://www.oeaw.ac.at/imafo/forschung/historische-identitaetsforschung/projekte/weitere-projekte/ostalpenraum-revisited/',
             'full_name': 'The Eastern Alps Revisited',
             'img': '/static/images/credits/logo_oar.jpg',
             'pi': 'Claudia Theune Vogt',
             'duration': '2012 - 2016',
             'text': """focused on the transformation of the late antique province of Noricum 
                         Mediterraneum into an area inhabited by a Slavic-speaking population that 
                         eventually became part of Bavaria. """}),
    ])
    return render_template('projects.html', projects=projects_)


@app.route('/team')
def team():
    return render_template('team.html')


@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html', e=e), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e), 404


@app.errorhandler(418)
def invalid_id(e):
    return render_template('418.html', e=e), 418
