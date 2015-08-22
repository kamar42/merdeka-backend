"""Local Development settings"""

from __future__ import absolute_import

from os.path import join, normpath

from .base import *

# change debug to true and template debug
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# database for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(PROJECT_ROOT, 'db.sqlite')),
    }
}

# cache config for local development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# adding apps for local development
INSTALLED_APPS += (
    'debug_toolbar',
)

# debug toolbar settings
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
DEBUG_TOOLBAR_PATCH_SETTINGS = False
