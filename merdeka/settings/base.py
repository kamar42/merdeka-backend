"""
Django settings for merdeka project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import abspath, basename, dirname, join, normpath
from sys import path

# absolute django project path
PROJECT_PATH = dirname(dirname(abspath(__file__)))

# absolute django project path to the top level project
PROJECT_ROOT = dirname(PROJECT_PATH)

# project name
PROJECT_NAME = basename(PROJECT_ROOT)

# apps root
APPS_ROOT = normpath(join(PROJECT_ROOT, PROJECT_NAME + '/apps/'))

# register apps root as path
path.append(APPS_ROOT)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-xekfuo=r^_ws(jn1g#5!+argpp*xiyjl4*1m7d3#=ecthjkvk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# set template debug to the same value with debug
TEMPLATE_DEBUG = DEBUG

# managers
ADMINS = (
    ('Ady Rahmat MA', 'adyrahmatma@gmail.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = []


# Application definition

BASE_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# project apps
PROJECT_APPS = (
    'merdeka.apps.base',
    'merdeka.apps.mdk',
)
# 3rd apps
THIRD_APPS = (
    'admin_honeypot',
)

# adding 3rd apps into installed apps
INSTALLED_APPS = BASE_APPS + PROJECT_APPS + THIRD_APPS

# setting admin honeypot
ADMIN_HONEYPOT_EMAIL_ADMINS = False

# set auth model
AUTH_USER_MODEL = 'base.MyUser'
# set authenticating backends
AUTHENTICATION_BACKENDS = (
    'merdeka.apps.base.backends.CustomMyUserBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'merdeka.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [normpath(join(PROJECT_ROOT, 'templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'merdeka.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# session and logging
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
