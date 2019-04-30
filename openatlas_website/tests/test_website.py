from openatlas_website.test_base import TestBaseCase

class WebsiteTests(TestBaseCase):

    def test_index(self):
        rv = self.app.get('/')
        assert b'OpenAtlas' in rv.data
