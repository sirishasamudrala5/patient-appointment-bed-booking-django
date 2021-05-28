import os
from coreApi.settings import *

DEBUG = False

SECRET_KEY = 'ee57=5vc=4wxkcf1044r1k8%d#*l-#&gu6xzl#-63=w3j1hd$e'
ALLOWED_HOSTS = '*'

DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'
DATABASES['default']['NAME'] = 'dialysiscenter'
DATABASES['default']['USER'] = 'postgres'
DATABASES['default']['PASSWORD'] = 'pass123'
DATABASES['default']['PORT'] = '5432'
