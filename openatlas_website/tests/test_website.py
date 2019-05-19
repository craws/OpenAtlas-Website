from openatlas_website.test_base import TestBaseCase


class WebsiteTests(TestBaseCase):

    def test_sites(self):
        assert b'OpenAtlas' in self.app.get('/').data
        assert b'Eichert' in self.app.get('/team').data
        assert b'MEDCON' in self.app.get('/projects').data
        assert b'Leeds' in self.app.get('/events').data
        assert b'404' in self.app.get('/whatever').data
