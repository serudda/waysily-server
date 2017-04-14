from django.db import models


class Feature(models.Model):
    """ Feature Model """
    feature_en = models.CharField(max_length=200, blank=True)
    feature_es = models.CharField(max_length=200, blank=True)
    description_en = models.TextField(max_length=1000, blank=True)
    description_es = models.TextField(max_length=1000, blank=True)
    active = models.BooleanField(default=False, verbose_name='Active')

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

