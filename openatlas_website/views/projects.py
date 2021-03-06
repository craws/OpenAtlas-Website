from collections import OrderedDict

from flask import render_template

from openatlas_website import app


@app.route('/projects')
def projects() -> str:
    projects_ = OrderedDict([
        ('MAMEMS', {
            'url': 'https://mamems.uni-mainz.de/',
            'full_name': 'Mount Athos in Medieval Eastern Mediterranean Society: Contextualizing the History of a Monastic Republic (ca. 850-1550)',
            'img': 'mamems.png',
            'image_license': 'CC-BY-SA 4.0, Jan Belik',
            'pi': 'Zachary Chitwood',
            'duration': '2020 - 2025',
            'institutes': ['JGU', 'OEAW', 'ACDH', 'ERC'],
            'text': """will constitute the first comprehensive examination of the monastic
                communities of Mount Athos as independent actors in medieval Eastern Mediterranean
                society."""}),
        ('THANADOS', {
            'url': 'https://thanados.net',
            'full_name': 'The Anthropological and Archaeological Database of Sepultures',
            'img': 'thanados.png',
            'image_license': 'CC-BY-SA 4.0, Jan Belik',
            'pi': 'Stefan Eichert, Nina Brundke',
            'duration': '2019 - 2021',
            'institutes': ['OEAW', 'OeAI', 'ACDH', 'NHM'],
            'text': """has the aim to create an online repository of all sepultures in nowadays Austria, dating to the Early Middle Ages (ca. 600-1100). It
                combines the three disciplines archaeology, anthropology and digital humanities.
                """}),
        ('HistoGenes', {
            'url': 'https://www.oeaw.ac.at/imafo/das-institut/detail/histogenes',
            'full_name': 'Integrating genetic, archaeological and historical perspectives on Eastern Central Europe, 400-900 AD',
            'img': 'histogenes.png',
            'image_license': 'CC-BY-SA 4.0, Dagmar Giesriegl',
            'pi': 'Walter Pohl',
            'duration': '2020 - 2026',
            'institutes': ['OEAW', 'IMAFO', 'ACDH', 'univie', 'NHM', 'MPI-SHH', 'IAS', 'ELTE',
                           'ERC'],
            'text': """is seeking to understand the impact of migrations and mobility on the
            population of the Carpathian Basin from 400-900 CE, based on a comprehensive
            analysis of samples from 6,000 ancient burial sites."""}),
        ('CONNEC', {
            'url': 'http://www.connectedclerics.com/',
            'full_name': 'Connected Clerics: Building a Universal Church in the Late Antique West (380-604 CE)',
            'img': 'connec.jpg',
            'image_license': 'CC-BY-SA 4.0, Sapfo Psani',
            'pi': 'David Natal',
            'duration': '2018 - 2022',
            'institutes': ['RHUL', 'OEAW', 'ACDH', 'ERC'],
            'text': """analyses how a ‘universal’ Late Antique Church was constructed despite the
                context of political fragmentation that precipitated the end of the Western
                Roman Empire and its division into smaller polities."""}),
        ('Moving Byzantium', {
            'url': 'https://www.oeaw.ac.at/en/imafo/research/byzantine-research/byzantium-and-beyond/mobility-and-intercultural-contacts/moving-byzantium',
            'full_name': 'Moving Byzantium',
            'img': 'moving_byzantium.jpg',
            'image_license': 'CC-BY-SA 4.0, Johannes Preiser-Kapeller',
            'pi': 'Claudia Rapp',
            'duration': '2015 - 2020',
            'institutes': ['OEAW', 'IMAFO', 'ACDH', 'FWF'],
            'text': """highlights the role of Byzantium as a global culture and analyses the
                internal flexibility of Byzantine society. Its main focuse is to contribute to a re-evaluation
                of a society and culture that has traditionally been depicted as stiff, rigid and
                encumbered by its own tradition."""}),
        ('MEDCEM', {
            'url': 'https://medcem.aiscr.cz/',
            'full_name': 'Medieval Cemeteries at the Periphery of the Carolingian World',
            'img': 'medcem.png',
            'image_license': 'CC-BY-SA 4.0, Jan Belik',
            'pi': 'Stefan Eichert',
            'duration': '2019 - ongoing',
            'institutes': ['MSMT', 'ARUP'],
            'text': """deals with the digital collection and presentation of medieval cemeteries and
                it is based at the Archaeological Institute of the Czech Academy of Sciences in
                Prague. All published information is provided online and can be explored via
                a digital catalogue and within an interactive map. Cartographic visualisations as well
                as charts and plots are created dynamically based on real archaeological research
                data."""}),
        ('MOP', {
            'url': 'https://oeaw.academia.edu/MapsofPower',
            'full_name': 'Maps of Power: Historical Atlas of Places, Borderzones and Migration Dynamics in Byzantium',
            'img': 'digtib.jpg',
            'image_license': 'CC-BY-SA 4.0, Jan Belik',
            'pi': 'Mihailo Popović (TIB PI: Balkans), Andreas Külzer (TIB PI: Asia Minor)',
            'duration': '2019 - ongoing',
            'institutes': ['OEAW', 'IMAFO', 'FWF', 'Byzantine Research', 'TIB', 'UAI'],
            'text': """is a sub-project of the Long-Term Project Tabula Imperii Byzantini (TIB) and
                part of the DigTIB initiative of the Austrian Academy of Sciences in Vienna. It
                creates, develops and upkeeps an online atlas of the Byzantine World. Selected parts from the
                rich data pool provided by TIB are extracted in order to digitally address
                new scholarly questions and methods."""}),
        ('PLAS', {
            'url': '',
            'full_name': 'The Prosopography of the Lascarid Period',
            'img': 'plas.jpg',
            'image_license': 'CC-BY-SA 4.0, Ekaterini Mitsiou and </br>Johannes Preiser-Kapeller',
            'pi': 'Ekaterini Mitsiou',
            'duration': '2018 - ongoing',
            'institutes': [],
            'text': """aims at creating a prosopographical database of Byzantium in the first half of the 13th
                century and mapping the complexities of a society in transition."""}),
        ('A Digital Geoportal of the History of the Serbs in Vienna (1741-1918)', {
            'url': 'https://orthodoxes-wien.oeaw.ac.at/',
            'full_name': 'A Digital Geoportal of the History of the Serbs in Vienna (1741-1918)',
            'img': 'openatlas.png',
            'image_license': 'CC-BY-SA 4.0, Jan Belik',
            'pi': 'Mihailo Popović',
            'duration': '2018 - 2019',
            'institutes': ['Wien Kultur', 'OEAW', 'IMAFO', 'Byzantine Research', 'AIT', 'BCM',
                           'NLS', 'Biblioteka Matice Srpske'],
            'text': """used biographical data on Orthodox 
                Serbs living in Vienna between 1741 and 1918 in order to illustrate how 
                Orthodox people began to migrate into the Habsburg Empire, how Orthodox merchants
                settled in Vienna and how they were integrated into Viennese society of that time."""}),
        ('DPP', {
            'url': 'https://dpp.oeaw.ac.at/',
            'full_name': 'Digitising Patterns of Power',
            'img': 'dpp.jpg',
            'image_license': 'CC-BY-SA 4.0, Jan Belik',
            'pi': 'Mihailo Popović',
            'duration': '2015 - 2019',
            'institutes': ['OEAW', 'IMAFO', 'univie'],
            'text': """focused on the analysis of the depiction of space in medieval written
                sources as well as the interaction between men-made and natural environment and the appropriation
                of space and the emergence of new political, religious and economic structures of
                power."""}),
        ('MEDCON', {
            'url': 'https://www.oeaw.ac.at/imafo/das-institut/detail/mapping-medieval-conflicts',
            'archive_url': 'http://hdl.handle.net/21.11115/0000-000C-D99B-1',
            'full_name': 'Mapping Medieval Conflict',
            'img': 'medcon.png',
            'image_license': 'CC-BY-SA 4.0, Jan Belik',
            'pi': 'Johannes Preiser-Kapeller',
            'duration': '2014 - 2017',
            'institutes': ['OEAW', 'IMAFO'],
            'text': """examined the explanatory power of concepts of social and spatial network
                analysis for phenomena of political conflict in medieval societies."""}),
        ("Frontier, Contact Zone or No Man's Land", {
            'url': 'https://openatlas.eu/gkn',
            'full_name': "Frontier, Contact Zone or No Man's Land",
            'img': 'frontier.png',
            'image_license': 'CC-BY-SA 4.0, Stefan Eichert',
            'pi': 'Stefan Eichert, Jiří Macháček',
            'duration': '2014 - 2017',
            'institutes': ['univie', 'MU', 'FWF', 'GACR'],
            'text': """is an international Austrian-Czech research project sponsored by the
                Austrian Science Fund (FWF) and Grantová agentura České republiky
                (GA ČR). It focused on the Morawa-Thaya region as boarder region between nowadays Austria and Czechia in Medieval times."""}),
         ('The Eastern Alps Revisited', {
             'url': 'https://www.oeaw.ac.at/imafo/forschung/historische-identitaetsforschung/projekte/weitere-projekte/ostalpenraum-revisited/',
             'full_name': 'The Eastern Alps Revisited',
             'img': 'ostalpen.png',
             'image_license': 'CC-BY-SA 4.0, Dagmar Giesriegl',
             'pi': 'Maximilian Diesenberger, Claudia Theune',
             'duration': '2012 - 2016',
             'institutes': ['OEAW', 'IMAFO', 'FWF'],
             'text': """focused on the transformation of the Late Antique province of Noricum
                 Mediterraneum into an area inhabited by a Slavic-speaking population that
                 eventually became part of Bavaria."""})])
    return render_template('projects.html', projects=projects_)
