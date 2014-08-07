"""
Django settings for timblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*mvh-h#06n(bvd$jnw@1v0flx5*()4%9mzp#+2fg5fm9h5w$fe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 1

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # 'django.contrib.comments',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_comments',
    'tagging',
    'mptt',
    'zinnia',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'zinnia.context_processors.version',  # Optional
)


ROOT_URLCONF = 'timblog.urls'

WSGI_APPLICATION = 'timblog.wsgi.application'

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'TimBlog',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # misc
    'LIST_PER_PAGE': 15
}

ZINNIA_ENTRY_CONTENT_TEMPLATES = [
  ('zinnia/_short_entry_detail.html', 'Short entry template'),
]

ZINNIA_ENTRY_DETAIL_TEMPLATES = [
    ('detail/fullwidth_entry_detail.html', 'Fullwidth template'),
]

# ZINNIA_SPAM_CHECKER_BACKENDS = ('zinnia.spam_checker.backends.mollom',)
# MOLLOM_PUBLIC_KEY = '3910a7e3cc27473d199d47b5c34c1d83'
# MOLLOM_PRIVATE_KEY = 'c24fe2e85556d997a0fb872d9136c53c'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#GMAIL SETTINGSsyv
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mubstimor@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['DJANGO_EMAIL_PASSWORD']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL='info@timblog.com'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC FILES CONFIG
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

ZINNIA_MEDIA_URL = os.path.join(MEDIA_URL, 'zinnia/')

# ZINNIA_UPLOAD_TO = 'uploads/zinnia'