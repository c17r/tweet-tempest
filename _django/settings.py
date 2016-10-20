import os
import environ
import json


def find_file(file_name, *args):
    for path in args:
        if os.path.isfile(path(file_name)):
            with path.file(file_name, 'r') as f:
                return f.read()
    return None

PROJECT_DIR = environ.Path(__file__) - 1
ROOT_DIR = environ.Path(__file__) - 2
SECRETS_DIR = environ.Path(__file__) - 3

SECRETS = json.loads(find_file('secrets.json', ROOT_DIR, SECRETS_DIR))

SECRET_KEY = SECRETS['DJANGO']['SECRET_KEY']
DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = '_django.wsgi.application'
ROOT_URLCONF = '_django.urls'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'social.apps.django_app.default',
    'webpack_loader',

    'backend',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
]

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

                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ROOT_DIR('db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
)

LOGIN_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_TWITTER_KEY = SECRETS['TWITTER']['CONSUMER_KEY']
SOCIAL_AUTH_TWITTER_SECRET = SECRETS['TWITTER']['CONSUMER_SECRET']
SOCIAL_AUTH_USER_MODEL = 'auth.User'
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    ROOT_DIR('frontend'),
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': ROOT_DIR('webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map'],
    }
}
