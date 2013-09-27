import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'local.db',
    }
}

TIME_ZONE = 'Europe/Paris'

LANGUAGE_CODE = 'fr-FR'

USE_I18N = False
USE_L10N = True
USE_TZ = True

SRC_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# static for our static files, media for user-uploaded pictures
MEDIA_ROOT = os.path.join(SRC_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(SRC_ROOT, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

SECRET_KEY = 'blop'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'sunspear.auth.AuthenticationMiddleware',
)

ROOT_URLCONF = 'sunspear.urls'
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (os.path.join(SRC_ROOT, 'templates'),)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.tz',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'sunspear',
)

LOGIN_URL = '/login'
LOGIN_EXEMPT_URLS = ['password/request', 'password/do', 'static/']
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SESSION_EXPIRE = 60*20

EMAIL_SUBJECT_PREFIX = '[Sunspear admin] '

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '{asctime} | {name:^12} | {levelname:^8} | {message}',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'handlers': {
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'include_html': True,
            'filters': ['require_debug_false'],
        },
    },
    'loggers': {
        'root': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
        },
    }
}
