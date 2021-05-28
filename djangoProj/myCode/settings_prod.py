import os
from myCode.settings import *
DEBUG = False

SECRET_KEY = '@bybyby05elmdujvrtdeetv+909ed2rkeittujqxow$czdemug'
ALLOWED_HOSTS = '*'
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'
DATABASES['default']['NAME'] = 'postgres'
DATABASES['default']['USER'] = 'postgres'
DATABASES['default']['PASSWORD'] = 'pass123'
DATABASES['default']['HOST'] = 'db'
DATABASES['default']['PORT'] = '5432'

# SECRET_KEY = os.environ['SECRET_KEY']
# ALLOWED_HOSTS = os.environ['HOST'].split(',')
# DATABASES['default']['ENGINE'] = os.environ['DB_ENGINE']
# DATABASES['default']['NAME'] = os.environ['DB_NAME']
# DATABASES['default']['USER'] = os.environ['DB_USER']
# DATABASES['default']['PASSWORD'] = os.environ['DB_PASSWORD']
# DATABASES['default']['HOST'] = os.environ['HOST']
# DATABASES['default']['PORT'] = os.environ['PORT']