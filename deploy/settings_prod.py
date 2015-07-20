# turn off debugging in production
DEBUG = False

# settings for the production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'djangousr',
        'PASSWORD': '1239087dfakjdhas#',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# allowed hosts for our production site
ALLOWED_HOSTS = ['46.101.26.90']

STATIC_ROOT = '/opt/mec_env/static/'
MEDIA_ROOT = '/opt/mec_env/media/'
