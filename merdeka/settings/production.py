"""Productions settings"""

from __future__ import absolute_import

from os import environ

from .base import *

# adding exception for improper configured settings
from django.core.exceptions import ImproperlyConfigured

def get_env_setting(setting):
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

# set allowed host, a must have configuration
ALLOWED_HOSTS = [*]

# set databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'merdeka',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}
