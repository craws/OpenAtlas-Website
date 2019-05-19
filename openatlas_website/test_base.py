# Created by Alexander Watzinger and others. Please see README.md for licensing information
import unittest

from openatlas_website import app


class TestBaseCase(unittest.TestCase):

    def setUp(self):
        print('hello')
        app.testing = True
        app.config['SERVER_NAME'] = 'localhost'
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['WTF_CSRF_METHODS'] = []  # This is the magic to disable CSRF for tests
        self.app = app.test_client()
