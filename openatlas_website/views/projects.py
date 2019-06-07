# Created by Alexander Watzinger and others. Please see README.md for licensing information
from collections import OrderedDict

from flask import render_template

from openatlas_website import app


@app.route('/projects')
def projects():
    projects_ = OrderedDict([
        ('THANADOS', {
            'url': 'https://www.oeaw.ac.at/stipendien-foerderungen/foerderprogramme/godigital/godigital-next-generation-ausgewaehlte-projekte/',
            'full_name': 'The Anthropological and Archaeological Database of Sepultures',
            'img': 'thanados.png',
            'image_license': 'CC-BY-SA 4.0, Jan Belik',
            'pi': 'Stefan Eichert, Nina Brundke',
            'duration': '2019 - 2022',
            'institutes': ['OEAW', 'OeAI', 'ACDH'],
            'text': """has the aim to create a repository of early medieval Austrian grave finds.
                It combines the three disciplines archaeology, anthropology and digital humanities.
                """}),
        ('CONNEC', {
            'url': 'http://www.connectedclerics.com/',
            'full_name': 'Connected Clerics: Building a Universal Church in the Late Antique West (380-604 CE)',
            'img': 'connec.jpg',
            'image_license': '',
            'pi': 'David Natal',
            'duration': '2018 - 2022',
            'institutes': ['RHUL', 'OEAW', 'ACDH', 'ERC'],
            'text': """analyses how a ‘universal’ late antique Church was constructed despite the
                context of political fragmentation that precipitated the end of the Western
                Roman Empire and its division into smaller polities."""}),
        ('DPP', {
            'url': 'https://dpp.oeaw.ac.at/',
            'full_name': 'Digitising Patterns of Power',
            'img': 'dpp.jpg',
            'image_license': 'CC-BY-SA 4.0, Jan Belik',
            'pi': 'Mihailo Popović',
            'duration': '2015 - 2019',
            'institutes': ['OEAW', 'IMAFO', 'univie'],
            'text': """focuses on the analysis of the depiction of space in medieval written
                sources, of the interaction between built and natural environment, of appropriation
                of space and the emergence of new political, religious and economic structures of
                power."""}),
        ('MEDCON', {
            'url': 'https://oeaw.academia.edu/MappingMedievalConflict',
            'full_name': 'Mapping Medieval Conflict',
            'img': 'medcon.png',
            'image_license': 'CC-BY-SA 4.0, Jan Belik',
            'pi': 'Johannes Preiser-Kapeller',
            'duration': '2014 - 2017',
            'institutes': ['OEAW', 'IMAFO'],
            'text': """examined the explanatory power of concepts of social and spatial network
                    analysis for phenomena of political conflict in medieval societies."""}),
        ("Frontier, Contact Zone or No Man's Land", {
            'url': 'http://www.openatlas.eu/gkn',
            'full_name': "Frontier, Contact Zone or No Man's Land",
            'img': 'frontier.png',
            'pi': 'Stefan Eichert, Jiří Macháček',
            'duration': '2014 - 2017',
            'institutes': ['univie', 'MU', 'FWF', 'GACR'],
            'text': """is an international Austrian-Czech research project sponsored by the
                Austrian Science Fund (FWF) and Grantová agentura České republiky
                (GA ČR)."""}),
         ('The Eastern Alps Revisited', {
             'url': 'https://www.oeaw.ac.at/imafo/forschung/historische-identitaetsforschung/projekte/weitere-projekte/ostalpenraum-revisited/',
             'full_name': 'The Eastern Alps Revisited',
             'img': 'ostalpen.png',
             'image_license': '',
             'pi': 'Maximilian Diesenberger, Claudia Theune Vogt',
             'duration': '2012 - 2016',
             'institutes': ['OEAW', 'IMAFO', 'FWF'],
             'text': """focused on the transformation of the late antique province of Noricum
                         Mediterraneum into an area inhabited by a Slavic-speaking population that
                         eventually became part of Bavaria. """})])
    return render_template('projects.html', projects=projects_)
