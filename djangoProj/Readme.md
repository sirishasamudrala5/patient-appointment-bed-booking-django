# Core API
Primary end-point invoked by the frontend. Handles authentication, permission management, database, patient appointment etc.

## pre requisites
python 3.7.3
pip 19.1.1
anaconda 4.6.11

## Project Setup
#### clone from git
```
git clone https://git.hashedin.com/sirisha.samudrala/huex-core-api.git
```

#### create a virtual environment 
```
pip install virtualenv
```
```
virtualenv <myenv>
```
```
activate <myenv>
```

#### In virtual environment <myenv> install all the dependencies
```
pip install -r requirements.txt
```

## Docker Setup

#### Build django web image using the dockerfile.
```
docker build -t django_web .
```

#### Ssh into the docker conatiner to verify if everything is working fine.
```
docker run -it django_web /bin/bash
```

#### Run
```
docker-compose run web python /code/manage.py migrate --noinput
```








