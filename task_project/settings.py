"""
Django settings for task_project project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l)(ro1def3#)!(y_1v3yau2#hs6g#!vjg_s!gq@kon&%7#&2mr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#PORTAL_URL = 'http://localhost:8000'
#LOGIN_URL = 'users:auth_login'



# Application definition

INSTALLED_APPS = [
    'task_app',
    

    #    for django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'django.contrib.admin',
    'django.contrib.sites',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms', 
    'django_coverage',

]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

REGISTRATION_OPEN = True
REGISTRATION_AUTO_LOGIN = True
ACCOUNT_ACTIVATION_DAYS = 365

MIDDLEWARE = [
    #'task_project.middleware.RequestTimeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'task_project.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
               # 'task_app.context_processors.task_processor',
            ],
        },
    },
]


WSGI_APPLICATION = 'task_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'task_db',
        'USER': 'task_db_user',
        'PASSWORD': '1592648t',
        #'USER': 'pyrigok',
        #'PASSWORD': '1592648',
        'HOST': 'localhost',

        # next - settings og test DB
        'TEST': {
            'NAME': 'test_task_db',
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')



    # for django-allauth
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 5

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


    # send email via google smtp server

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'pyrigechok@gmail.com'
EMAIL_HOST_PASSWORD = '1592648732648qqq'


    # for 'django_coverage'
from django.conf import settings

# Specify the coverage test runner
COVERAGE_TEST_RUNNER = getattr(settings, 'COVERAGE_TEST_RUNNER',
                             'django_coverage.coverage_runner.CoverageRunner')

# Specify whether coverage data file is created or not.
COVERAGE_USE_CACHE = getattr(settings, 'COVERAGE_USE_CACHE', False)

# Specify regular expressions of code blocks the coverage analyzer should
# ignore as statements (e.g. ``raise NotImplemented``).
# These statements are not figured in as part of the coverage statistics.
# This setting is optional.
COVERAGE_CODE_EXCLUDES = getattr(settings, 'COVERAGE_CODE_EXCLUDES',[
                                    'def __unicode__\(self\):',
                                    'def get_absolute_url\(self\):',
                                    'from .* import .*', 'import .*',
                                 ])

# Specify a list of regular expressions of paths to exclude from
# coverage analysis.
# Note these paths are ignored by the module introspection tool and take
# precedence over any package/module settings such as:
# TODO: THE SETTING FOR MODULES
# Use this to exclude subdirectories like ``r'.svn'``, for example.
# This setting is optional.
COVERAGE_PATH_EXCLUDES = getattr(settings, 'COVERAGE_PATH_EXCLUDES',
                                 [r'.svn'])

# Specify a list of additional module paths to include
# in the coverage analysis. By default, only modules within installed
# apps are reported. If you have utility modules outside of the app
# structure, you can include them here.
# Note this list is *NOT* regular expression, so you have to be explicit,
# such as 'myproject.utils', and not 'utils$'.
# This setting is optional.
COVERAGE_ADDITIONAL_MODULES = getattr(settings, 'COVERAGE_ADDITIONAL_MODULES', [])

# Specify a list of regular expressions of module paths to exclude
# from the coverage analysis. Examples are ``'tests$'`` and ``'urls$'``.
# This setting is optional.
COVERAGE_MODULE_EXCLUDES = getattr(settings, 'COVERAGE_MODULE_EXCLUDES',
                                   ['tests$', 'settings$', 'urls$', 'locale$',
                                    'common.views.test', '__init__', 'django',
                                    'migrations'])


# Specify the directory where you would like the coverage report to create
# the HTML files.
# You'll need to make sure this directory exists and is writable by the
# user account running the test.
# You should probably set this one explicitly in your own settings file.

#COVERAGE_REPORT_HTML_OUTPUT_DIR = '/my_home/test_html'
COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'coverage')

# True => html reports by 55minutes
# False => html reports by coverage.py
COVERAGE_CUSTOM_REPORTS = getattr(settings, 'COVERAGE_CUSTOM_REPORTS', True)


# True => Always output coverage reports to STDOUT.
# False => Don't output coverage reports to STDOUT.
# (not set) => output coverage reports to STDOUT only if COVERAGE_REPORT_HTML_OUTPUT_DIR is not set or None.
#
# This makes it possible to both generate HTML reports and see coverage
# information on STDOUT.
COVERAGE_USE_STDOUT = getattr(settings, 'COVERAGE_USE_STDOUT', COVERAGE_REPORT_HTML_OUTPUT_DIR is None)

# The name of the folder within utils/coverage_report/badges/ that
# contains the badges we want to use.
COVERAGE_BADGE_TYPE = getattr(settings, 'COVERAGE_BADGE_TYPE', 'drone.io')