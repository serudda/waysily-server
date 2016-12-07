from django.db import models
from locations.models import Location

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

    TYPE_CHOICES = (
        ('H', 'Community Tutor'),
        ('P', 'Professional Teacher'),
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

    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    teacher_since = models.CharField(max_length=4)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Experience(models.Model):
    """ Experience Model """

    teacher = models.ForeignKey(Teacher, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=2, blank=True)
    date_start = models.CharField(max_length=4, blank=True)
    date_finish = models.CharField(max_length=4, blank=True)
    description = models.CharField(max_length=200, blank=True)
