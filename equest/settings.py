

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'bim#)dwgy98$hq0o(2bqi8+shw(s0u7!zh_i&eqfaodwu=^ihe'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True


from decouple import config
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)



ALLOWED_HOSTS = ['equests.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'apps.core',
    'apps.quiz',
    'apps.game',
    'apps.relatorio',

    # libs
    'django',
    'crispy_forms',
    'django_tables2',
    'django_extensions',
    'rest_framework',
    'sweetify',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'equest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'equest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

from dj_database_url import parse as dburl
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = { 'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


LOGIN_REDIRECT_URL = 'begin'
LOGOUT_REDIRECT_URL = '/'


# login redirect
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/'

# Model de autenticacao
AUTH_USER_MODEL = 'core.User'

# Sobreescrevendo template django-tables2 com metronic table
# DJANGO_TABLES2_TEMPLATE = BASE_DIR+'/apps/core/templates/metronic-table.html'
DJANGO_TABLES2_TEMPLATE = BASE_DIR+'/apps/core/templates/metronic-table.html'


CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'