# Don't edit this file. To override settings please use instance/production.py
from flask import Config

VERSION = '0.1.0'
LANGUAGES = {'en': 'English', 'de': 'Deutsch'}
DEBUG = False
SECRET_KEY = 'CHANGE ME'

# Security
SESSION_COOKIE_SECURE = False  # Should be True in production.py if using HTTPS
REMEMBER_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = "AAaajjjfk887856$%kk"
