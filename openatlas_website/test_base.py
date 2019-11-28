import unittest

from openatlas_website import app


class TestBaseCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.config['SERVER_NAME'] = 'localhost'
        self.app = app.test_client()
