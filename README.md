# **Waysily BackEnd Structure**

##Overview

It's a base structure (Full Stack Single Page Application) for the starter who want to start a web application.
This repository has 2 separate modules: **Client** module and **Server** module.

###Client

Client side contains the following technologies:

* [Angular 1.5.8](https://github.com/angular/angular.js)
* [Typescript 1.8.10] (https://www.typescriptlang.org)
* [Sass](http://sass-lang.com)
* [Gulp](http://gulpjs.com)
* [Bower](https://bower.io)
* [npm 3.9.5] (https://www.npmjs.com)

###Server

Server side was made with the following technologies:

* [Python 3.5](https://www.python.org/downloads/)
* [Django 1.10](https://www.djangoproject.com/)
* [Django REST Framework](http://www.django-rest-framework.org/)


## Getting Started

You have to install previously:

* Python 3.5
* NodeJS (npm)
* Gem (Ruby)
* Virtualenv (optional)

You have to git clone this repository:
```
git clone https://github.com/sergioruizdavila/asanni-backend.git
```

### Installation for REST API Server Side

Open a terminal **(on root project/server)**:

1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt` if you have error with 'docutils' package, you can uninstall it: `pip uninstall docutils`
4. make migrations (**next** topic)
5. create a superusers ('**create superuser**' topic)

#### Make migrations

On Django when you create a new model of data (example: posts model, authentication model, etc) you have to create a specific migration for each model.

In this case, we have djangoapps/authentication model and djangoapps/posts model (the latter, I leave it as an example for when you need to create a new app in the future).

In order to create migrations for each models (in this case 'authentication' and 'posts') you have to:
`python manage.py makemigrations <app_label>` in our case would be `python manage.py makemigrations authentication` and `python manage.py makemigrations posts`

In order to see If you create each migrations well you can use the following command:
`python manage.py showmigrations`
You should see the migrations list, including 'authentication' and 'posts' models (with X).

To run each migrations:

- `python manage.py migrate`


#### Create Superuser

In order to test that all it's right, you should create a superuser in order to LogIn on Django Rest Admin Page:

- `python manage.py createsuperuser`


#### Usage for REST API Server

Here if everything is OK, you should run server and go to localhost on browser, you should be able to see Django Rest Admin Page.

- `python manage.py runserver`


**Reference:** [https://github.com/shalomeir/snippod-starter-demo-app-server](https://github.com/shalomeir/snippod-starter-demo-app-server)
