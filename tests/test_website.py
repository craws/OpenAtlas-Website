import unittest

from flask import url_for

from openatlas_website import app


class TestBaseCase(unittest.TestCase):

    def setUp(self) -> None:
        app.testing = True
        app.config['SERVER_NAME'] = 'local.host'
        self.app = app.test_client()


class WebsiteTests(TestBaseCase):

    def test_sites(self) -> None:
        with app.app_context():
            assert b'OpenAtlas' in self.app.get('/').data
            assert b'Eichert' in self.app.get(url_for('team')).data
            assert b'MEDCON' in self.app.get(url_for('projects')).data
            assert b'Leeds' in self.app.get(url_for('events')).data
            assert b'interactive' in self.app.get(url_for('features')).data
            assert b'ACDH' in self.app.get(url_for('cooperation')).data
            assert b'Principal' in \
                   self.app.get(url_for('cooperation_information')).data
            assert b'Flask' in self.app.get(url_for('software')).data
            assert b'THANADOS' in self.app.get(url_for('news')).data
            assert b'404' in self.app.get('/whatever').data
            assert 'x00' in str(self.app.get('/static/favicon.ico').data)
