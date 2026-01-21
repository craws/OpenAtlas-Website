from typing import Any

tags = {
    'topic': [
        'Anthropology',
        'Archaeology',
        'Cultural-Heritage',
        'Epigraphy',
        'History',
        'Prosopography'],
    'status': [
        'Ongoing',
        'Concluded',
        'Presentation-Site',
        'Archived',
        'Cooperation']}

projectList: dict[str, Any] = {
    'Epigraphies of Pious Travel': {
        'url':
            'https://www.oeaw.ac.at/en/byzanz/gesellschaft-und-'
            'landschaft/epigraphik/epigraphies-of-pious-travel',
        'full_name': 'Epigraphies of Pious Travel',
        'frontend': 'https://mobyz-atlas.openatlas.eu/',
        'img': 'pious_travel.png',
        'image_license': 'CC-BY 4.0, Rachael Griffiths',
        'pi': 'Rachael Helen Banes, Andreas Rhoby',
        'duration': '2021 - ongoing',
        'institutes': ['OEAW', 'IMAFO', 'ACDH', 'FWF'],
        'tags': [
            'Ongoing',
            'History',
            'Epigraphy',
            'Cooperation',
            'Presentation-Site'],
        'text':
            '(FWF project I 5286-G25) collates '
            'and contextualises graffiti written by pilgrims in the eastern '
            'Mediterranean during the Byzantine period, c. 300 – 1500 CE. '
            'Through collaboration with OpenAtlas, the project will produce a '
            'digital corpus of material in the Greek language. Not reliant on '
            'a wealthy patron, graffiti written by pilgrims provides an '
            'insight into Byzantine religious ritual and the experiences of a '
            'larger cross-section of the population.'},
    'ENCHANT': {
        'url':
            'https://www.oeaw.ac.at/en/imafo/research/byzantine-research/'
            'byzantium-and-beyond/mobility-and-intercultural-contacts/'
            'entangled-charters-of-anatolia-1200-1300-enchant',
        'full_name': 'Entangled Charters of Anatolia (1200-1300)',
        'frontend': 'https://discover-plas.openatlas.eu/',
        'img': 'enchant.png',
        'image_license': 'CC-BY-SA 4.0, Johannes Preiser-Kapeller',
        'pi': 'Johannes Preiser-Kapeller ',
        'duration': '2023 - 2026',
        'institutes': ['OEAW', 'IMAFO', 'ACDH', 'univie', 'FWF'],
        'tags': ['Ongoing', 'History', 'Cooperation', 'Presentation-Site'],
        'text':
            '(FWF P 36403-G), aims to provide a comparison based on a '
            'systematic survey of important artefacts of these efforts, i. e. '
            'the documents issued by the state chancelleries of the Byzantine '
            '“empires in exile” of Nicaea and Trebizond, Cilician Armenia and '
            'the Seljuk Sultanate. The project provides a digital catalogue, '
            'a corpus of those documents whose texts have been transmitted at '
            'least in significant parts, and a number of publications '
            'presenting a comparative analysis of these multifaceted acts '
            'of “world (re)ordering” after crisis.'},
    'FemCareVienna': {
        'url': 'https://discover-femcarevienna.openatlas.eu/',
        'full_name': 'FemCareVienna',
        'frontend': 'https://discover-femcarevienna.openatlas.eu/',
        'img': 'femcare.jpg',
        'image_license': 'CC-BY-SA 4.0, Jasmin Hangartner/ Novetus GmbH',
        'pi': 'Michaela Binder',
        'duration': '2023 - 2026',
        'institutes': ['Novetus', 'OEAW', 'ACDH', 'FWF'],
        'tags': [
            'Ongoing',
            'Archaeology',
            'History',
            'Anthropology',
            'Cooperation',
            'Presentation-Site'],
        'text':
            '(FWF individual grant P 36459-G) aims to elucidate the history '
            'of medical care for woman through an interdisciplinary study of '
            'the historical and bioarchaeological record pertaining to the '
            'Hospital of the Elisabethians in Vienna. Central to the project '
            'are the life histories of 390 patients from the 18th century '
            'whose skeletal human remains were excavated from the hospital '
            'cemetery.'},
    'bITEM': {
        'url': 'https://bitem.at',
        'frontend': 'https://bitem.at/',
        'full_name': 'Beyond the Item',
        'img': 'bitem.png',
        'image_license': 'CC-BY-SA 4.0, Jan Belik',
        'pi': 'Viola Winkler, Roland Filzwieser',
        'duration': '2023 - 2025',
        'institutes': ['NHM', 'LBI', 'OEAW', 'ACDH'],
        'tags': [
            'Archaeology',
            'Concluded',
            'History',
            'Cooperation',
            'Presentation-Site'],
        'text':
            ' - short for Beyond the Item - Biographies and '
            'Itineraries of Cultural Heritage Objects in Museums and beyond - '
            'aims to present well-known museum objects in a state-of-the-art '
            'web application that is freely accessible online. The objects '
            'and their biographies are vividly described and, in addition to '
            'images and texts, 3D models as digital twins, timelines, and '
            'story maps are made available.'},
    'Approaching Byzantium': {
        'url':
            'https://www.byzanz-mainz.de/en/research/project-details/'
            'approaching-byzantium-in-ottoman-istanbul-the-reception-of-the-'
            'byzantine-heritage-of-constantinople-by-scholars-from-the-holy-'
            'roman-empire-in-the-16th-century',
        'full_name':
            'Approaching Byzantium in Ottoman Istanbul: the Reception of the '
            'Byzantine Heritage of Constantinople by Scholars from the Holy '
            'Roman Empire in the 16th century',
        'img': 'approaching_byzantium.png',
        'frontend': 'https://approaching-byzantium.openatlas.eu/',
        'image_license': 'CC-BY-SA 4.0, Jan Belik',
        'pi': 'Nicholas Melvani',
        'duration': '2021 - 2025',
        'institutes': ['JGU', 'OEAW', 'ACDH', 'DFG', 'Leibnitz Byzanz'],
        'tags': [
            'Concluded',
            'History',
            'Prosopography',
            'Cooperation',
            'Presentation-Site'],
        'text':
            'analyzes how visiting the city of Constantinople affected the '
            'reception of Byzantium by humanists from the Holy Roman Empire in'
            ' the 16th century, when the former Byzantine capital was the seat'
            ' of the Ottoman Empire.'},
    'MAMEMS': {
        'url': 'https://mamems.uni-mainz.de/',
        'full_name':
            'Mount Athos in Medieval Eastern Mediterranean Society: '
            'Contextualizing the History of a Monastic Republic '
            '(ca. 850-1550)',
        'img': 'mamems.png',
        'image_license': 'CC-BY-SA 4.0, Jan Belik',
        'frontend': 'https://discover-mamems.openatlas.eu/',
        'pi': 'Zachary Chitwood',
        'duration': '2020 - 2025',
        'institutes': ['JGU', 'OEAW', 'ACDH', 'ERC'],
        'tags': [
            'Concluded',
            'History',
            'Prosopography',
            'Cooperation',
            'Presentation-Site'],
        'text':
            'will constitute the first comprehensive examination of the '
            'monastic communities of Mount Athos as independent actors in '
            'medieval Eastern Mediterranean society.'},
    'DANCEM': {
        'url':
            'https://www.leibniz-gwzo.de/en/research/humans-and-environment/'
            'borders-formation-structure-and-shifts/late-antique-cemeteries',
        'full_name': 'Late antique cemeteries on the Danube',
        'img': 'dancem.jpg',
        'image_license': 'CC-BY-SA 4.0. Birte Janzen/Kristin Opitz',
        'pi': 'Kristin Opitz',
        'duration': '2020 - ongoing',
        'institutes': ['GWZO', 'Stadtmuseum_St_Poelten'],
    'tags': ['Ongoing', 'Archaeology', 'Anthropology'],
        'text':
            'focuses on bringing together and analysing both published and'
            ' self-compiled archaeological and anthropological data from late'
            ' antique cemeteries on the Danube Limes and its hinterland '
            'between Passau and Budapest to gain deeper insights into the '
            'lives and deaths of the people.'},
    'MEDCEM': {
        'url': 'https://thanados.net/about/medcem',
        'frontend': 'https://thanados.net/',
        'full_name':
            'Medieval Cemeteries at the Periphery of the Carolingian World',
        'img': 'medcem.png',
        'image_license': 'CC-BY-SA 4.0, Jan Belik',
        'pi': 'Stefan Eichert',
        'duration': '2019 - ongoing',
        'institutes': ['MSMT', 'ARUP'],
        'tags':
            ['Ongoing', 'Archaeology', 'Anthropology', 'Presentation-Site'],
        'text':
            'deals with the digital collection and presentation of medieval '
            'cemeteries and it is based at the Archaeological Institute of the'
            ' Czech Academy of Sciences in Prague. All published information '
            'is  provided online and can be explored via a digital catalogue '
            'and  within an interactive map. Cartographic visualisations as '
            'well as charts and plots are created dynamically based on real '
            'archaeological research data.'},
    'MOP': {
        'url': 'https://maps-of-power.oeaw.ac.at/',
        'full_name': 'Maps of Power',
        'img': 'mop.jpg',
        'image_license': 'CC-BY-SA 4.0, Jan Belik',
        'pi': 'Mihailo St. Popović',
        'duration': '2019 - ongoing',
        'institutes':
            ['OEAW', 'IMAFO', 'FWF', 'Byzantine Research', 'TIB', 'UAI'],
        'tags': ['Ongoing', 'History', 'Prosopography'],
        'text':
            'is a research initiative that serves the methodological '
            'and interdisciplinary networking of scholars from the field of '
            'Historical Geography. It focuses on Historical Ecology, Sacred '
            'Topography and Cultural Heritage and sees itself as a scholarly '
            'platform that implements its own projects based on OpenAtlas as '
            'well as networks in an interdisciplinary fashion through joint '
            'projects.'},
    'PLAS': {
        'url': '',
        'full_name': 'The Prosopography of the Lascarid Period',
        'img': 'plas.jpg',
        'frontend': 'https://discover-plas.openatlas.eu/',
        'image_license':
            'CC-BY-SA 4.0, Ekaterini Mitsiou and <br>'
            'Johannes Preiser-Kapeller',
        'pi': 'Ekaterini Mitsiou',
        'duration': '2018 - ongoing',
        'institutes': [],
        'tags': ['Ongoing', 'History', 'Prosopography', 'Presentation-Site'],
        'text':
            'aims at creating a prosopographical database of Byzantium in the '
            'first half of the 13th century and mapping the complexities of a '
            'society in transition.'},
    'Shahi': {
        'url': 'https://shahimaterialculture.univie.ac.at/',
        'frontend': 'https://shahi.acdh.oeaw.ac.at/',
        'full_name':
            'Cultural Formation and Transformation: Shahi Art and Architecture'
            ' from Afghanistan to the West Tibetan Frontier at the Dawn of the'
            ' Islamic Era',
        'img': 'shahi.jpg',
        'image_license': '',
        'pi':
            'Deborah Klimburg-Salter;'
            'National research partner: Michael Alram',
        'duration': '2018 - 2023',
        'institutes': ['univie', 'OEAW', 'ACDH', 'FWF', 'KHM', 'CIRDIS'],
        'tags':
            ['Concluded', 'Archaeology', 'Cooperation', 'Presentation-Site'],
        'text':
            '(FWF, P-31246) considers for the first time the Shahi kingdoms '
            '(c. 7th-10th centuries) which played a pivotal role in the '
            'history of Central, Inner, and South Asia. Our ongoing research '
            'on the primary source material--artifacts, coins, inscriptions, '
            'archaeological evidence--suggests that the Hindu-Buddhist culture'
            ' survived through the end of the first millennium and gradually '
            'evolved towards an Islamic culture at the start of the second '
            'millennium.'},
    'INDIGO': {
        'url': 'https://projectindigo.eu',
        'full_name': 'INventory and DIsseminate Graffiti along the dOnaukanal',
        'img': 'indigo.jpeg',
        'image_license': 'CC-BY-SA 4.0, Geert Verhoeven',
        'pi': 'Geert Verhoeven, Norbert Pfeifer',
        'duration': '2021 - 2023',
        'institutes': [
            'LBI', 'TUGG', 'OEAW', 'ACDH', 'Wien', 'SprayCity', 'GIFLE',
            'VRVIS'],
        'tags': ['Concluded', 'Cultural-Heritage', 'Cooperation'],
        'text':
            'aims to build the basis to systematically document, monitor, '
            'disseminate, and analyse 7 km of graffiti along Vienna’s Danube '
            'Canal in the next decade.'},
    'THANADOS': {
        'url': 'https://thanados.net',
        'frontend': 'https://thanados.net',
        'full_name':
            'The Anthropological and Archaeological Database of Sepultures',
        'img': 'thanados.png',
        'image_license': 'CC-BY-SA 4.0, Jan Belik',
        'pi': 'Stefan Eichert, Nina Richards',
        'duration': '2019 - 2021',
        'institutes': ['OEAW', 'OeAI', 'ACDH', 'NHM'],
        'tags': [
            'Concluded',
            'Archaeology',
            'Anthropology',
            'Cooperation',
            'Presentation-Site'],
        'text':
            'has the aim to create an online repository of all sepultures in '
            'nowadays Austria, dating to the Early Middle Ages (ca. 600-1100).'
            ' It combines the three disciplines archaeology, anthropology and '
            'digital humanities.'},
    'CONNEC': {
        'url': 'https://discover-connec.openatlas.eu/',
        'frontend': 'https://discover-connec.openatlas.eu/',
        'full_name':
            'Connected Clerics: Building a Universal Church in the Late '
            'Antique West (380-604 CE)',
        'img': 'connec.jpg',
        'image_license': 'CC-BY-SA 4.0, Sapfo Psani',
        'pi': 'David Natal',
        'duration': '2018 - 2022',
        'institutes': ['RHUL', 'OEAW', 'ACDH', 'ERC'],
        'tags': [
            'Concluded',
            'History',
            'Prosopography',
            'Cooperation',
            'Presentation-Site'],
        'text':
            'analyses how a ‘universal’ Late Antique Church was constructed '
            'despite the context of political fragmentation that precipitated '
            'the end of the Western  Roman Empire and its division into '
            'smaller polities.'},
    'Moving Byzantium': {
        'url':
            'https://www.oeaw.ac.at/en/imafo/research/byzantine-research/'
            'byzantium-and-beyond/mobility-and-intercultural-contacts/'
            'moving-byzantium',
        'full_name': 'Moving Byzantium',
        'frontend': 'https://mobyz-atlas.openatlas.eu/',
        'img': 'moving_byzantium.jpg',
        'image_license': 'CC-BY-SA 4.0, Johannes Preiser-Kapeller',
        'pi': 'Claudia Rapp',
        'duration': '2015 - 2020',
        'institutes': ['OEAW', 'IMAFO', 'ACDH', 'FWF'],
        'tags': [
            'Concluded',
            'History',
            'Prosopography',
            'Cooperation',
            'Presentation-Site'],
        'text':
            'highlights the role of Byzantium as a global culture and analyses'
            ' the internal flexibility of Byzantine society. Its main focus is'
            ' to contribute to a re-evaluation of a society and culture that '
            'has traditionally been depicted as stiff, rigid and encumbered by'
            ' its own tradition.'},
    'A Digital Geoportal of the History of the Serbs in Vienna (1741-1918)': {
        'url': 'https://orthodoxes-wien.oeaw.ac.at/',
        'frontend': 'https://geoportal.orthodoxes-europa.at/',
        'full_name':
            'A Digital Geoportal of the History of the Serbs '
            'in Vienna (1741-1918)',
        'img': 'geoportal.png',
        'image_license': 'CC-BY-SA 4.0, Jan Belik',
        'pi': 'Mihailo Popović',
        'duration': '2018 - 2019',
        'institutes': [
            'Wien Kultur', 'OEAW', 'IMAFO', 'Byzantine Research', 'AIT', 'BCM',
            'NLS', 'Biblioteka Matice Srpske'],
        'tags': ['Concluded', 'History', 'Prosopography', 'Presentation-Site'],
        'text':
            'used biographical data on Orthodox Serbs living in Vienna '
            'between 1741 and 1918 in order to illustrate how Orthodox people '
            'began to migrate into the Habsburg Empire, how Orthodox '
            'merchants settled in Vienna and how they were integrated into '
            'Viennese society of  that time.'},
    'DPP': {
        'url': 'https://dpp.oeaw.ac.at/',
        'full_name': 'Digitising Patterns of Power',
        'img': 'dpp.jpg',
        'image_license': 'CC-BY-SA 4.0, Jan Belik',
        'pi': 'Mihailo Popović',
        'duration': '2015 - 2019',
        'institutes': ['OEAW', 'IMAFO', 'univie'],
        'tags': ['Concluded', 'History', 'Prosopography', 'Cooperation'],
        'text':
            'focused on the analysis of the depiction of space in medieval '
            'written sources as well as the interaction between men-made and '
            'natural environment and the appropriation of space and the '
            'emergence of new political, religious and economic structures of '
            'power.'},
    'MEDCON': {
        'url':
            'https://www.oeaw.ac.at/imafo/das-institut/'
            'detail/mapping-medieval-conflicts',
        'archive_url': 'http://hdl.handle.net/21.11115/0000-000C-D99B-1',
        'full_name': 'Mapping Medieval Conflict',
        'img': 'medcon.png',
        'image_license': 'CC-BY-SA 4.0, Jan Belik',
        'pi': 'Johannes Preiser-Kapeller',
        'duration': '2014 - 2017',
        'institutes': ['OEAW', 'IMAFO'],
        'tags': [
            'Concluded', 'History', 'Prosopography', 'Cooperation',
            'Archived'],
        'text':
            'examined the explanatory power of concepts of social and spatial '
            'network analysis for phenomena of political conflict in medieval '
            'societies.'},
    "Frontier, Contact Zone or No Man's Land": {
        'url': 'https://openatlas.eu/gkn',
        'full_name': "Frontier, Contact Zone or No Man's Land",
        'img': 'frontier.png',
        'image_license': 'CC-BY-SA 4.0, Stefan Eichert',
        'pi': 'Stefan Eichert, Jiří Macháček',
        'duration': '2014 - 2017',
        'institutes': ['univie', 'MU', 'FWF', 'GACR'],
        'tags': ['Concluded',  'Archaeology'],
        'text':
            'is an international Austrian-Czech research project sponsored by '
            'the Austrian Science Fund (FWF) and Grantová agentura České '
            'republiky (GA ČR). It focused on the Morawa-Thaya region as '
            'boarder region between nowadays Austria and Czechia in Medieval '
            'times.'},
    'The Eastern Alps Revisited': {
        'url':
            'https://www.oeaw.ac.at/imafo/forschung/'
            'historische-identitaetsforschung/projekte/weitere-projekte/'
            'ostalpenraum-revisited/',
        'full_name': 'The Eastern Alps Revisited',
        'img': 'ostalpen.png',
        'image_license': 'CC-BY-SA 4.0, Dagmar Giesriegl',
        'pi': 'Maximilian Diesenberger, Claudia Theune',
        'duration': '2012 - 2016',
        'institutes': ['OEAW', 'IMAFO', 'FWF'],
        'tags': ['Concluded',  'Archaeology'],
        'text':
            'focused on the transformation of the Late Antique province of '
            'Noricum Mediterraneum into an area inhabited by a Slavic-speaking'
            ' population that eventually became part of Bavaria.'}}
