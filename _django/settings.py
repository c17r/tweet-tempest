import os
import environ
import json

PROJECT_DIR = environ.Path(__file__) - 1
ROOT_DIR = environ.Path(__file__) - 2

env = environ.Env(
    DJANGO_SECRET=(str, 'default-key-needs-to-be-changed'),
    TWITTER_CONSUMER_KEY=(str, ''),
    TWITTER_CONSUMER_SECRET=(str, '')
)
environ.Env.read_env(str(ROOT_DIR.path('.env')))

SECRET_KEY = env('DJANGO_SECRET')
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
    'social_django',
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

    'social_django.middleware.SocialAuthExceptionMiddleware',
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

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
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
    'social_core.backends.twitter.TwitterOAuth',
)

LOGIN_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_TWITTER_KEY = env('TWITTER_CONSUMER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = env('TWITTER_CONSUMER_SECRET')
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
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': ROOT_DIR('webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
    }
}
