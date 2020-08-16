# Yuva Parivartan

![](https://img.shields.io/github/license/CybSec-NITW/WeaponHEX)
![](https://img.shields.io/pypi/pyversions/django.svg)

Source code of the project

## Instructions

Make sure you have Git and Python installed on your machine. If not, you can download and install them from here: https://git-scm.com/downloads https://www.python.org/downloads/

Open a terminal and change current directory to your dev or projects folder.

Then follow these steps
```
$ pip install virtualenv
$ mkdir codeforgood
$ cd codeforgood
$ git clone https://github.com/IndiaCFG3/team-38.git .
// A login would be required since it is a private repository
$ virtualenv -p python3 .
$ .\Scripts\activate                               #For MAC/Linux -> . bin/activate
(codeforgood) $ pip install -r requirements.txt
(codeforgood) $ cd src
(codeforgood) $ python manage.py makemigrations #For MAC/Linux -> python3 manage.py makemigrations
(codeforgood) $ python manage.py migrate        #For MAC/Linux -> python3 manage.py migrate
(codeforgood) $ python manage.py runserver      #For MAC/Linux -> python3 manage.py runserver
It will deploy the website on your localhost https://127.0.0.1:8000
```

## Admin login

Django provides a default admin interface which can be used to perform create, read, update and delete operations on the models and manage users directly.

```
Go to directory containing manage.py file and enter the following command to create a new superuser

$ python manage.py createsuperuser

Enter the details. After successful creation open https://127.0.0.1:8000/admin and use your login credentials.
```

PS : You can use git GUI clients such as GitKraken or SourceTree to manage your projects.
