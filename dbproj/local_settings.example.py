from settings import *

SECRET_KEY = 'oo8=+1)kmkf)j5bs5m45l4z3xw+sijm^vm@j)-)d)3bpv-4gc9'

# Enable Debugging
#DEBUG = True

# Allowed Hosts
ALLOWED_HOSTS = ['www.example.com']

STATIC_ROOT = '/srv/www.example.com/static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'CONN_MAX_AGE': 14400, # 8h set; use 4h
        'NAME': 'dbname',
        'USER': 'username',
        'PASSWORD': 'password',
        # https://blog.ionelmc.ro/2014/12/28/terrible-choices-mysql
        'OPTIONS': {
            'sql_mode': 'TRADITIONAL',
            'charset': 'utf8',
            'init_command': 'SET '
                'default_storage_engine=INNODB,'
                'character_set_connection=utf8,'
                'collation_connection=utf8_bin;'
                'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED',
        }  # Now we have a mild degree of confidence :-)
    }
}

INSTALLED_APPS += []
