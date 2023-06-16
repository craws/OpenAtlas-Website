def release_text(news_id: int) -> str:
    return \
        'A new software version of OpenAtlas is available, see ' \
        '<a target="_blank" ' \
        f'href="https://redmine.openatlas.eu/news/{news_id}">' \
        'release notes</a>.'


news_ = {
    'News': {
        '2023-05-06': {
            'date': '2023-05-06',
            'title': 'OpenAtlas version 7.13.0',
            'text': release_text(30)},
        '2023-04-27': {
            'date': '2023-04-27',
            'title': 'New OpenAtlas cooperation with bITEM',
            'text':
                'We are happy to announce a new cooperation with bITEM '
                '<br>You can find more details at the '
                '<a target="_blank" href="/projects">projects</a> page.'},
        '2023-04-01': {
            'date': '2023-04-01',
            'title': 'OpenAtlas version 7.12.0 and mission statement',
            'text': release_text(29) +
            '<br>Also, we like to introduce our new website layout and '
            'our <a href="/mission">mission statement<a>.'},
        '2023-02-19': {
            'date': '2023-02-19',
            'title': 'OpenAtlas version 7.11.0',
            'text': release_text(28)},
        '2023-02-04': {
            'date': '2023-02-04',
            'title': 'OpenAtlas version 7.10.0 and a welcome',
            'text': release_text(27) +
            '<br>Also, a warm welcome to our archiving expert '
            'Massimiliano Carloni.'},
        '2023-01-01': {
            'date': '2023-01-01',
            'title': 'OpenAtlas version 7.9.0',
            'text': release_text(26)}},
    '2022': {
        '2022-12-01': {
            'date': '2022-12-01',
            'title': 'First (early) version of OpenAtlas-Discovery released',
            'text':
                'The first version of <a target="_blank" '
                'href="https://github.com/craws/OpenAtlas-Discovery">'
                'OpenAtlas-Discovery</a> is released. '
                'It is a general presentation site for data of OpenAtlas '
                'projects and can also be used as starting point for more '
                'specialised presentation sites. A preview with demo data is '
                'available here: '
                '<a  target="_blank" '
                'href="https://frontend-demo-dev.openatlas.eu">Demo</a>'},
        '2022-11-18': {
            'date': '2022-11-18',
            'title': 'OpenAtlas version 7.8.0',
            'text': release_text(25)},
        '2022-10-18': {
            'date': '2022-10-18',
            'title': 'OpenAtlas version 7.7.0 and a welcome',
            'text': release_text(24) +
            '<br>And a warm welcome to our new frontend developer '
            'Moritz "Mocca" Großfurtner.'},
        '2022-08-25': {
            'date': '2022-08-25',
            'title': 'OpenAtlas version 7.6.0',
            'text': release_text(23)},
        '2022-08-18': {
            'date': '2022-08-18',
            'title': 'OpenAtlas version 7.5.0 and a welcome',
            'text':
                release_text(22) +
                '<br>And a warm welcome to our new intern Laura Kremser'},
        '2022-06-10': {
            'date': '2022-06-10',
            'title': 'OpenAtlas version 7.4.0',
            'text': release_text(21)},
        '2022-05-08': {
            'date': '2022-05-08',
            'title': 'OpenAtlas version 7.3.0',
            'text': release_text(20)},
        '2022-04-15': {
            'date': '2022-04-15',
            'title': 'New OpenAtlas cooperation with Approaching Byzantium',
            'text':
                'We are happy to announce a new cooperation with Approaching '
                'Byzantium.<br>You can find more details at the '
                '<a target="_blank" href="/projects">projects</a> page.'},
        '2022-04-02': {
            'date': '2022-04-02',
            'title': 'OpenAtlas version 7.2.0 and a welcome back',
            'text':
                release_text(19) +
                '<br>And a warm welcome back to the team to Veronika '
                'Gründhammer'},
        '2022-02-15': {
            'date': '2022-02-15',
            'title': 'OpenAtlas version 7.1.0',
            'text': release_text(18)},
        '2022-01-01': {
            'date': '2022-01-01',
            'title': 'OpenAtlas version 7.0.0 and a welcome',
            'text':
                release_text(17) +
                '<br>And a warm welcome to our newest team member Andi '
                '(Andreas Olschnögger)'}},
    '2021': {
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
                'International Medieval Congress</a>.<br>Please check '
                'out session 118, 1001, and 1519 '
                '<a target="_blank" '
                'href="https://www.imc.leeds.ac.uk/imc-2021/">here</a>'},
        '2021-06-18': {
            'date': '2021-06-18',
            'title':
                'OpenAtlas at the "Medieval Mount Athos between Wealth and '
                'Poverty" conference',
            'text':
                'To join the conference (17th and 18th of June), check out the'
                ' <a target="_blank" href="'
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
                'href="https://twitter.com/OpenAtlas_eu/">Twitter</a> and feel'
                ' free to follow and retweet'},
        '2021-05-17': {
            'date': '2021-05-17',
            'title': 'New OpenAtlas cooperation with Shahi',
            'text':
                'We are happy to announce a new cooperation with Shahi.'
                '<br>You can find more details at the '
                '<a target="_blank" href="/projects">projects</a> page.'},
        '2021-05-08': {
            'date': '2021-05-08',
            'title': 'OpenAtlas version 6.2.0',
            'text': release_text(12)},
        '2021-04-15': {
            'date': '2021-04-15',
            'title': 'OpenAtlas at DHA Twitter Schaukasten',
            'text':
                'OpenAtlas is part of the DHaustria Twitter conference. '
                'Check #digitalDHaustria on Twitter or <a target="_blank"'
                'href='
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
                '<a href="https://archiv.chnt.at/chnt-25-2020-proceedings/" '
                'target="_blank">25th CHNT-Conference</a>'}}}
