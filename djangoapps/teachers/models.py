from django.db import models
from locations.models import Location
from django.core.validators import validate_comma_separated_integer_list


class Language(models.Model):
    """ Language Model """

    native = models.CharField(max_length=200, null=True, blank=True)
    learn = models.CharField(max_length=200, null=True, blank=True)
    teach = models.CharField(max_length=200, null=True, blank=True)


class Teacher(models.Model):
    """ Teacher Model """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    """ Basic Information """
    location = models.ForeignKey(Location, null=True, blank=True)
    languages = models.ForeignKey(Language, null=True, blank=True)

    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField(max_length=50)
    born = models.CharField(max_length=100)
    about = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

