# Waysily Server project

This real-world project of: http://www.waysily.com, a platform to join students with language teachers and language school. Feel free to use the code and the information from this project, if you have any question you could write us on Twitter: [@seruda](https://www.twitter.com/seruda) or [@rosa7082](https://www.twitter.com/rosa7082)

## Tools used

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
git clone https://github.com/sruda/waysily-server.git
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


# Note:

If you have any problem to run this project, feel free to ping us!

P.S. You can find the client-side of this project here:

[https://github.com/sruda/waysily-client](https://github.com/sruda/waysily-client)

It's based on: AngularJS (1.5.8) + Typescript + Gulp + Sass
