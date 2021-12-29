def release_text(news_id: int) -> str:
    return \
        f'A new software version of OpenAtlas is available, see ' \
        f'<a target="_blank" ' \
        f'href="https://redmine.openatlas.eu/news/{news_id}">' \
        f'release notes</a>'


news_items = {
    'News': {
        '2021-11-18': {
            'date': '2021-11-18',
            'title': 'OpenAtlas version 6.6.0',
            'text': release_text(16)},
        '2021-09-19': {
            'date': '2021-09-19',
            'title': 'OpenAtlas version 6.5.0',
            'text': release_text(15)},
        '2021-08-10': {
            'date': '2021-08-10',
            'title': 'OpenAtlas version 6.4.0',
            'text': release_text(14)},
        '2021-07-05': {
            'date': '2021-07-05 to 2021-07-09',
            'title': 'Several OpenAtlas team members present at the IMC Leeds',
            'text':
                'Several papers regarding OpenAtlas will be presented at the '
                '<a target="_blank" '
                'href="https://www.imc.leeds.ac.uk/imc-2021/">'
                'International Medieval Congress</a> this week. Please check '
                'out session 118, 1001, and 1519'
            '<a target="_blank" '
            'href="https://www.imc.leeds.ac.uk/imc-2021/">here</a>'},
        '2021-06-18': {
            'date': '2021-06-18',
            'title':
                'OpenAtlas at the "Medieval Mount Athos between Wealth and '
                'Poverty" conference',
            'text':
                'To join the conference (17th and 18th of June), check out the '
                '<a target="_blank" href="'
                'https://mamems.uni-mainz.de/conference-medieval-mount-athos-'
                'between-wealth-and-poverty/">MAMENS homepage</a>'},
        '2021-06-13': {
            'date': '2021-06-13',
            'title': 'OpenAtlas version 6.3.0',
            'text': release_text(13)},
        '2021-05-25': {
            'date': '2021-05-25',
            'title': 'OpenAtlas joined Twitter',
            'text':
                'Check out @OpenAtlas_eu on <a target="_blank" '
                'href="https://twitter.com/OpenAtlas_eu/">Twitter</a> and feel '
                'free to follow and retweet'},
        '2021-05-17': {
            'date': '2021-05-17',
            'title': 'New OpenAtlas cooperation with SHAHI',
            'text':
                'We are happy to announce a new cooperation. For project '
                'details, see <a target="_blank" '
                'href="https://shahimaterialculture.univie.ac.at/">SHAHI</a>'},
        '2021-05-08': {
            'date': '2021-05-08',
            'title': 'OpenAtlas version 6.2.0',
            'text': release_text(12)},
        '2021-04-15': {
            'date': '2021-04-15',
            'title': 'OpenAtlas at DHA Twitter Schaukasten',
            'text':
                'OpenAtlas is part of the DHaustria Twitter conference. '
                'Check #digitalDHaustria on Twitter or <a target="_blank" href='
                '"https://digital-humanities.at/en/dha/s-project/openatlas">'
                'here</a>'},
        '2021-04-05': {
            'date': '2021-04-05',
            'title': 'OpenAtlas version 6.1.0',
            'text': release_text(11)},
        '2021-03-13': {
            'date': '2021-03-13',
            'title': 'OpenAtlas version 6.0.0',
            'text': release_text(9)},
        '2021-01-21': {
            'date': '2021-01-21',
            'title': 'THANADOS at Der Standard archeology blog',
            'text':
                'An <a target="_blank" '
                'href="https://www.derstandard.at/story/2000123448701/'
                'tausende-graeber-zum-selbsterforschen"> article </a>(German) '
                'about THANADOS was released at "Der Standard"'},
        '2021-01-16': {
            'date': '2021-01-16',
            'title': 'OpenAtlas version 5.7.0',
            'text': release_text(8)}},
    '2020': {
        '2020-11-30': {
            'date': '2020-11-30',
            'title': 'OpenAtlas version 5.6.0',
            'text': release_text(7)},
        '2020-11-06': {
            'date': '2020-11-06',
            'title': 'THANADOS: Best App Award',
            'text':
                'Winning Best App Award for <a target="_blank" '
                'href="https://thanados.net">THANADOS</a> at '
                '<a href="https://www.chnt.at/chnt25-over" target="_blank">'
                '25th CHNT-Conference</a>'}}}
