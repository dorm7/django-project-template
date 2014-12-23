# Django Template for Dorm7

This is a django template for dorm7

## INSTALLATION & SETTINGS

### Install Django

To install django, first go to your virtualenv, and then run the following command:

    sudo pip install django
    
### Create Django project from the template

To create the project, run the following command and please replace your\_project_name to what you like :

    django-admin.py startproject --template=https://github.com/dorm7/django-project-template/archive/master.zip --extension=py,rst,html your_project_name


### Setting Virtualenv

At first, you should make sure you have [virtualenv](http://www.virtualenv.org/) installed. 

after that, just cd to your\_project_name:

   cd your\_project_name

Then create your virtualenv:

    virtualenv venv
    
Second, you need to enable the virtualenv by

	source venv/bin/activate
	



### Install requirements

For development:

    pip install -r requirements/local.txt

For production:

    pip install -r requirements.txt

For heroku:

Use requirements-heroku.txt to replace requirements.txt


### Start To Run

to start project.  cd your\_project_name again (find manage.py )

```bash
python manage.py migrate   # you just do it once

python manage.py runserver
```

feel free to visit [http://127.0.0.1:8000/style_guide/](http://127.0.0.1:8000/style_guide/) and edit _varialbe.scss, you will see the amazing starting style guide for the project

	
