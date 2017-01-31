
from django.db import models


class Feedback(models.Model):
    """ Feedback Model """
    uid = models.CharField(max_length=200)
    next_country = models.CharField(max_length=2, blank=True)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

