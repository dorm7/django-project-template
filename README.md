# Django Template for Dorm7

This is a django template for dorm7

## INSTALLATION & SETTINGS

### Setting Virtualenv

At first, you should make sure you have [virtualenv](http://www.virtualenv.org/) installed. Then create your virtualenv:

    virtualenv test_project
    
Second, you need to enable the virtualenv by

	source test_project/bin/activate
	

### Install Django

To install django, first go to your virtualenv, and then run the following command:

    pip install django

### Create Django project from the template

To create the project, run the following command:

    django-admin.py startproject --template=https://github.com/dorm7/django-project-template/archive/master.zip --extension=py,rst,html test_project

### Install requirements

For development:

    pip install -r requirements/local.txt

For production:

    pip install -r requirements.txt

For heroku:

Use requirements-heroku.txt to replace requirements.txt
