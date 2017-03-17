from django.db import models

from djangoapps.globals.enums.models import CountriesList


class Position(models.Model):
    """ Position Model """
    uid = models.CharField(max_length=200)
    lng = models.CharField(max_length=60, null=True, blank=True, verbose_name='Longitude on Google Map')
    lat = models.CharField(max_length=60, null=True, blank=True, verbose_name='latitude on Google Map')

    def __str__(self):
        return "Position (lng, lat) id: " + str(self.id)


class Location(models.Model):
    """ Location Model """
    position = models.OneToOneField(Position, related_name='position', on_delete=models.CASCADE, null=True,
                                    verbose_name='Position on Google Map')

    uid = models.CharField(max_length=200)
    country = models.CharField(max_length=2, choices=CountriesList.COUNTRIESLIST_CHOICES, blank=True, default='',
                               verbose_name='Location Country')
    address = models.CharField(max_length=100, blank=True, verbose_name='Location Address')
    city = models.CharField(max_length=110, blank=True, verbose_name='Location City')
    state = models.CharField(max_length=110, blank=True, verbose_name='Location State')
    zip_code = models.CharField(max_length=20, blank=True, verbose_name='Location ZipCode')

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Location id: " + str(self.id)
