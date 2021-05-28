FROM python:3.7.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip

# Install Deploy Dependencies
RUN pip install psycopg2==2.8.3 
RUN pip install gunicorn==19.9.0
RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE coreApi.settings_prod

COPY . /code/