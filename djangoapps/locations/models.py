from django.db import models


class Position(models.Model):
    """ Position Model """
    lng = models.CharField(max_length=50, null=True, blank=True)
    lat = models.CharField(max_length=50, null=True, blank=True)


class Location(models.Model):
    """ Location Model """
    position = models.ForeignKey(Position, null=True, blank=True)

    country = models.CharField(max_length=2, blank=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

