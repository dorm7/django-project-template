from base import *
import dj_database_url

DATABASES['default'] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    'storages',
    'gunicorn',
)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

ALLOWED_HOSTS = []

AWS_ACCESS_KEY_ID = get_env_setting(AWS_ACCESS_KEY_ID)
AWS_SECRET_ACCESS_KEY = get_env_setting(AWS_SECRET_ACCESS_KEY)
AWS_STORAGE_BUCKET_NAME = ''

S3_BASE_URL = ''
MEDIA_URL = '//%s/%s/' % (S3_BASE_URL, AWS_STORAGE_BUCKET_NAME)
STATIC_URL = '//%s/%s/' % (S3_BASE_URL, AWS_STORAGE_BUCKET_NAME)

AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False
