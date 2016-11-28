from django.core.validators import RegexValidator
from django.db import models
from rest_framework.settings import api_settings


class Teacher(models.Model):
    """ Teacher Model """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField(max_length=50)
    born = models.CharField(max_length=100)
    about = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)