from collections import OrderedDict

from flask import render_template

from openatlas_website import app


@app.route('/events')
def events() -> str:
    upcoming = OrderedDict([
        ('2021-06-17',
         {'country': 'Germany',
          'city': 'Mainz',
          'institute': 'Johannes Gutenberg University',
          'name': 'Medieval Mount Athos: Wealth and Poverty',
          'link': 'https://mamems.uni-mainz.de/',
          'title': 'OpenAtlas - An Introduction'}),
        ('2021-07-05',
         {'country': 'United Kingdom',
          'city': 'Leeds',
          'institute': 'University of Leeds',
          'name': 'International Medieval Congress 2021',
          'link': 'https://www.imc.leeds.ac.uk/2021-climates/',
          'title': 'OpenAtlas: How to Reference Historical Points in Space and Time'}),
        ('2021-07-08',
            {'country': 'United Kingdom',
             'city': 'Leeds',
             'institute': 'University of Leeds',
             'name': 'International Medieval Congress 2021',
             'link': 'https://www.imc.leeds.ac.uk/2021-climates/',
             'title': 'Digital Tools for Historical Research: A Round Table Discussion'})])
    past = OrderedDict([
        ('2020', OrderedDict([
            ('2020-11-06', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'Wien Museum and Stadtarchäologie Wien',
                            'name': '25th CHNT-Conference',
                            'title': 'Winning Best App Award for <a target="_blank" href="https://thanados.net">THANADOS</a>',
                            'link': 'https://www.chnt.at/chnt25-over'}),
            ('2020-07-23', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'WUK',
                            'title': 'OpenAtlas Summer Meeting'}),
            ('2020-06-17', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'Natural History Museum Vienna',
                            'name': 'OpenAtlas Hackathon',
                            'link': 'https://redmine.openatlas.eu/projects/uni/wiki/Hackathon_2020-06-17'}),
            ('2020-02-11', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'Austrian Centre for Digital Humanities',
                            'name': 'ACDH-CH - Meet the Researchers',
                            'link': 'https://www.oeaw.ac.at/acdh/education/acdh-ch-internships/meet-the-researchers-programme',
                            'title': 'OpenAtlas',
                            'docs': {
                                'Presentation': '2020-02-11_OpenAtlas_Meet_the_Researchers.pdf'}}),
        ])),
        ('2019', OrderedDict([
            ('2019-12-04', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'Austrian Academy of Sciences',
                            'name': 'Fourth HistGeo Lecture',
                            'link': 'https://histgeo.oeaw.ac.at/category/histgeo-lecture/',
                            'title': 'THANADOS – The Anthropological and Archaeological Database of Sepultures'}),
            ('2019-10-24', {'country': 'United Kingdom',
                            'city': 'London',
                            'institute': 'Royal Holloway',
                            'name': 'OpenAtlas Workshop',
                            'link': 'https://www.eventbrite.co.uk/e/introducing-openatlas-tickets-77159242371',
                            'title': 'Introducing OpenAtlas',
                            'docs': {'Presentation': '2019-10-24_OpenAtlas_London.pdf'}}),
            ('2019-10-18', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'Austrian Academy of Sciences',
                            'name': 'Byzantino-Serbian Borderzones in Transition',
                            'title': 'OpenAtlas',
                            'docs': {'Program': '2019-10_18_Byzantino-Serbian_Borderzones_in_Transition.pdf',
                                     'Presentation': '2019-10-18_OpenAtlas_DIGTIP_german.pdf'}}),
            ('2019-07-16', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'Austrian Centre for Digital Humanities',
                            'name': 'ACDH-CH - Meet the Researchers',
                            'link': 'https://www.oeaw.ac.at/acdh/education/acdh-ch-internships/meet-the-researchers-programme',
                            'title': 'Introduction to CIDOC CRM with OpenAtlas as an example use case'}),
            ('2019-07-03', {'country': 'United Kingdom',
                            'city': 'Leeds',
                            'institute': 'University of Leeds',
                            'name': 'International Medieval Congress 2019',
                            'link': 'https://www.imc.leeds.ac.uk/imc2019/',
                            'title': 'OpenAtlas - An open source application to map historical data with CIDOC CRM',
                            'docs': {'Presentation': '2019-07-03_OpenAtlas.pdf'}}),
            ('2019-06-18', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'WUK',
                            'title': 'OpenAtlas and THANADOS Summer Meeting'}),
            ('2019-05-16', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'Austrian Academy of Sciences',
                            'name': 'Digitising Patterns of Power - Book and Project Presentation',
                            'title': 'OpenAtlas unter die Haube geschaut',
                            'link': 'https://www.oeaw.ac.at/en/detail/news/landkarten-der-macht/',
                            'docs': {'Program': '2019-05-16_Programm_DPP.pdf',
                                     'Presentation': '2019-05-16_dpp_book_presentation.pdf'}}),
            ('2019-02-20', {'country': 'Czech Republic',
                            'city': 'Prague',
                            'institute': 'Institute of Archaeology of the Czech Academy of Sciences',
                            'title': 'Networking meeting with AIS'}),
            ('2019-02-13', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'University of Vienna',
                            'name': 'Prosopography Hackathon',
                            'link': 'https://acdh.univie.ac.at/nachrichten/single-view/news/linking-past-people-a-prosopography-hackathon-at-the-uni-of-vienna/?tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Baction%5D=detail&cHash=b3c6c21d5d122910b03f0c0b3f65228e',
                            })])),
        ('2018', OrderedDict([
            ('2018-10-19', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'Austrian Academy of Sciences',
                            'name': 'DPP Concluding Conference',
                            'link': 'https://dpp.oeaw.ac.at/conference/index.php?site=program',
                            'title': 'OpenAtlas - How to Grow Software for Historians',
                            'docs': {'Program': '2018-10-19_dpp_concluding_programm.pdf',
                                     'Presentation': '2018-10-19_dpp_concluding.pdf'}}),
            ('2018-07-03', {'country': 'United Kingdom',
                            'city': 'Leeds',
                            'institute': 'University of Leeds',
                            'name': 'International Medieval Congress 2018',
                            'link': 'https://www.imc.leeds.ac.uk/imcarchive/2018/sessions/840/',
                            'title': 'OpenAtlas - How to Grow Software for Historians',
                            'docs': {'Presentation': '2018-07-03_leeds.pdf'}}),
            ('2018-05-29', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'Austrian Centre for Digital Humanities',
                            'name': 'ACDH-CH Tool Gallery - CIDOC CRM',
                            'link': 'https://www.oeaw.ac.at/acdh/events/event-series/acdh-tool-gallery-41',
                            'title': 'OpenAtlas',
                            'docs': {'Presentation': '2018-05-29_ACDH_Tool_Gallery.pdf'}})])),
        ('2017', OrderedDict([
            ('2017-07-03', {'country': 'United Kingdom',
                            'city': 'Leeds',
                            'institute': 'University of Leeds',
                            'name': 'International Medieval Congress 2017',
                            'link': 'http://imc.leeds.ac.uk/dbsql02/AQueryServlet?*id=30&*formId=30&*context=IMC&conference=2017&sessionId=7539&chosenPaperId=&*servletURI=https://imc.leeds.ac.uk/dbsql02/AQueryServlet',
                            'title': 'Relational Modelling of Historical Data - Concepts and Challenges',
                            'docs': {'Paper': '2017-07-03_Concepts_and_Challanges.pdf',
                                     'Presentation': '2017-07-03_leeds.pdf'}}),
            ('2017-06-20', {'country': 'Germany',
                            'city': 'Bochum',
                            'institute': 'Ruhr-University Bochum',
                            'name': 'Regesten und Register, Netzwerke und Karten',
                            'title': 'OpenAtlas',
                            'docs': {'Presentation': '2017-06-20_bochum.pdf'}})])),
        ('2016', OrderedDict([
            ('2016-09-28', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'Institute for Medieval Research',
                            'name': 'Digitising Patterns of Power',
                            'link': 'https://dpp.oeaw.ac.at/workshop/',
                            'title': 'OpenAtlas',
                            'docs': {'Presenation': '2016-09-28_dpp.pdf'}}),
            ('2016-07-08', {'country': 'United Kingdom',
                            'city': 'Leeds',
                            'institute': 'University of Leeds',
                            'name': 'International Medieval Congress 2016',
                            'link': 'https://www.imc.leeds.ac.uk/imcarchive/2016/sessions/803/',
                            'title': 'Relational Modelling of Historical Data - A Technical Perspective',
                            'docs': {'Paper': '2016-07-05_A_Technical_Perspective.pdf',
                                     'Presentation': '2016-07-05_leeds.pdf'}}),
            ('2016-04-13', {'country': 'Austria',
                            'city': 'Vienna',
                            'institute': 'Institute for Medieval Research',
                            'name': 'Entangled Worlds Congress',
                            'link': 'https://www.dasanderemittelalter.net/conference-entangled-worlds/',
                            'title': 'OpenAtlas',
                            'docs': {'Presentation': '2016-04-13_entangled_worlds.pdf'}})])),
        ('2015', OrderedDict([
            ('2015-12-16', {'country': 'Czech Republic',
                            'city': 'Brno',
                            'institute': 'Masaryk University',
                            'title': 'OpenAtlas Workshop'})]))])
    return render_template('events.html', past=past, upcoming=upcoming)
