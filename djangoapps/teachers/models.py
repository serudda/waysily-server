from django.core.validators import RegexValidator
from django.db import models

class Teacher(models.Model):
    """ Teacher Model """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    country_birth = models.CharField(max_length=100)
    city_birth = models.CharField(max_length=100)
    state_birth = models.CharField(max_length=100)
    country_live_in = models.CharField(max_length=100)
    city_live_in = models.CharField(max_length=100)
    state_live_in = models.CharField(max_length=100)
    address_live_in = models.CharField(max_length=100)
    native_languages_regex = RegexValidator(regex=r'^[1-8](,[1-8])*$', message="This field must be a integers list")
    native_languages = models.CharField(validators=[native_languages_regex], max_length=200)
    languages_speak_regex = RegexValidator(regex=r'^[1-8](,[1-8])*$', message="This field must be a integers list")
    languages_speak = models.CharField(validators=[languages_speak_regex], max_length=200)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)