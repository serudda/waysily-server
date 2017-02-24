from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver

from djangoapps.locations.models import Location


# LANGUAGE CLASS
class Language(models.Model):
    """ Language Model """

    native = ArrayField(models.CharField(max_length=200), blank=True)
    learn = ArrayField(models.CharField(max_length=200), blank=True)
    teach = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return "Language " + str(self.id)


# PROFILE CLASS
class Profile(models.Model):
    """ Profile Model """

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    """ Profile Information """
    user = models.OneToOneField(User, primary_key=True, related_name='user', on_delete=models.CASCADE)
    languages = models.OneToOneField(Language, related_name='languages', on_delete=models.CASCADE, null=True)
    location = models.OneToOneField(Location, related_name='location', on_delete=models.CASCADE, null=True)
    about = models.TextField(max_length=10000, default='', blank=True)
    phone_number = models.CharField(max_length=30, default='', blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    born_country = models.CharField(max_length=2, blank=True)
    born_city = models.CharField(max_length=110, blank=True)
    avatar = models.TextField(max_length=5000, default='', blank=True)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user.save()

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
