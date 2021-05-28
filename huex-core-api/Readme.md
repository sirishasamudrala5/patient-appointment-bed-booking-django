# Core API
Primary end-point invoked by the frontend. Handles authentication, permission management, database, patient appointment etc.

## API Documentation
After successful installation , go to [Swagger](http://127.0.0.1:8000/swagger/) for API documentation

## pre requisites
python 3.7.3  
pip 19.1.1  
Postgresql

## Project Setup
#### clone from git
```
git clone https://git.hashedin.com/sirisha.samudrala/huex-core-api.git
```

#### create a virtual environment 
```
$ pip install virtualenv
$ virtualenv <myenv>
$ activate <myenv>
```

#### In virtual environment <myenv> install all the dependencies
```
$ pip install -r requirements.txt
```

#### Run the code
```
$ python manage.py runserver
```

#### MAke your DB ready
Run this command to import all the tables into your postgresql Database
```
$ python manage.py migrate
```

#### Create Super user to access Django Admin
```
$ python manage.py createsuperuser
```

after registering as a super user , you can now run the server and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to access the Django admin portal where you can add/modify/delete users.

#### Run UnitTestcases
```
$ python manage.py test
```
