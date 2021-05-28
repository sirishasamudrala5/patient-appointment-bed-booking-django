# Planning API
Given patients and their preferred slots, create an appointment plan with the least cost keeping preferred time in mind.

## pre requisites
python 3.7.3  
pip 19.1.1

## Project Setup
#### clone from git
```
git clone https://git.hashedin.com/sirisha.samudrala/huex-planning-api.git
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

#### Create Super user to access Django Admin
```
$ python manage.py createsuperuser
```

after registering as a super user , you can now run the server and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to access the Django admin portal where you can add/modify/delete users.

#### Run UnitTestcases
```
$ python manage.py test
```







