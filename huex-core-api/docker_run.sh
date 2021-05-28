docker run\
 -e SECRET_KEY="ee57=5vc=4wxkcf1044r1k8%d#*l-#&gu6xzl#-63=w3j1hd$e"\
 -e HOST="*" \
  -e DB_ENGINE="django.db.backends.postgresql" \
  -e DB_NAME="dialysiscenter" \
  -e DB_USER="postgres" \
  -e DB_PASSWORD="pass123" \
  -e DB_PORT="5432" \
  --add-host=database:"192.168.0.102" \
  -p 8000:8000 \
  django_corpapi \
  "$@"