#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import logging

from os.path import dirname, abspath, realpath, join as path_join


DIR_PATH = abspath(dirname(realpath(__file__)))
EXTRA_LIB_PATH = [
    path_join(DIR_PATH, 'lib'),
    path_join(DIR_PATH, 'lib', 'libs.zip'),
    dirname(DIR_PATH),
]
sys.path = EXTRA_LIB_PATH + sys.path

# Local imports go here.

logging.basicConfig(level=logging.DEBUG)

def sanitize_url(url):
    if not url.endswith('/'):
        url = url + '/'
    return url

# See http://code.google.com/appengine/articles/gdata.html
APPLICATION_ID = os.environ['APPLICATION_ID']
APPLICATION_NAME = 'Tata Institute of Social Sciences HRM and LR'
APPLICATION_URL = "tiss-secure.appspot.com"
SERVER_PORT = os.environ['SERVER_PORT']
SERVER_NAME = os.environ['SERVER_NAME']
SERVER_SOFTWARE = os.environ['SERVER_SOFTWARE']
PRODUCTION_HTTP_PORT = 80
#DEPLOYMENT_MODE = 'development' if 'Development' in SERVER_SOFTWARE else 'production'
if SERVER_PORT and SERVER_PORT != str(PRODUCTION_HTTP_PORT):
    DEPLOYMENT_MODE = 'development'
    HOST_NAME = '%s:%s' % (SERVER_NAME, SERVER_PORT)
else:
    DEPLOYMENT_MODE = 'production'
    HOST_NAME = SERVER_NAME

#logging.debug(HOST_NAME)

NO_REPLY_EMAIL = 'no-reply@tisshrmlr.edu.in'
ADMIN_EMAIL = 'administrator@tisshrmlr.edu.in'

if DEPLOYMENT_MODE == 'development':
    LOCAL = True
    DEBUG = True
    ABSOLUTE_ROOT_URL = 'http://%s:%s/' %(SERVER_NAME, SERVER_PORT)
    PRIMARY_URL = '/'
    SECURE_URL = '/'
    MINIFIED = ''
    #MINIFIED = '-min'
else:
    LOCAL = False
    DEBUG = True
    ABSOLUTE_ROOT_URL = 'http://tiss-secure.appspot.com/'
    PRIMARY_URL = 'http://tiss-secure.appspot.com/'
    SECURE_URL = 'https://%s.appspot.com/' % APPLICATION_ID
    MINIFIED = '-min'


MEDIA_URL = '%ss/' % PRIMARY_URL

TEMPLATE_BUILTINS = {
    'LOCAL': LOCAL,
    'APPLICATION_NAME': APPLICATION_NAME,
    'APPLICATION_URL': sanitize_url(APPLICATION_URL),
    'ABSOLUTE_ROOT_URL': sanitize_url(ABSOLUTE_ROOT_URL),
    'MEDIA_URL': sanitize_url(MEDIA_URL),
    'PRIMARY_URL': sanitize_url(PRIMARY_URL),
    'SECURE_URL': sanitize_url(SECURE_URL),
    'TEMPLATE_DEBUG': DEBUG,
    'MINIFIED': MINIFIED,
}

TEMPLATE_DIRS = [
    path_join(DIR_PATH, 'templates'),
]

