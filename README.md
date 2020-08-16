# Verilog Master

![](https://img.shields.io/github/license/CybSec-NITW/WeaponHEX)
![](https://img.shields.io/pypi/pyversions/django.svg)

Verilog is a hardware descriptive language used to model modern day digital systems like flip-flops, memories and microprocessors. It is a very powerful tool to design and simulate digital hardwares at any level.

This project is about providing an interactive environment for hardware enthusiasts to learn this language.

## Instructions

Make sure you have Git and Python installed on your machine. If not, you can download and install them from here: https://git-scm.com/downloads https://www.python.org/downloads/

Open a terminal and change current directory to your dev or projects folder.

Then follow these steps
```
$ pip install virtualenv
$ mkdir verilog-master
$ cd verilog-master
$ git clone https://github.com/Rushikesh1008/Verilog-Master.git .
$ virtualenv -p python3 .
$ .\Scripts\activate                               #For MAC/Linux -> . bin/activate
(verilog-master) $ pip install -r requirements.txt
(verilog-master) $ cd src
(verilog-master) $ python manage.py makemigrations #For MAC/Linux -> python3 manage.py makemigrations
(verilog-master) $ python manage.py migrate        #For MAC/Linux -> python3 manage.py migrate
(verilog-master) $ python manage.py runserver      #For MAC/Linux -> python3 manage.py runserver
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
