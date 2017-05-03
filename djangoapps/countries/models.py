from django.contrib.sites.models import Site
from django.db import models


class Country(models.Model):
    """ Country Model """

    alias_country = models.CharField(
        default='',
        max_length=250,
        unique=True,
        verbose_name='Alias Country',
        help_text='Example: "new-zealand" (name splitted by - )'
    )
    code = models.CharField(max_length=2, blank=True, verbose_name='Country Code')
    name_es = models.CharField(max_length=200, default='', verbose_name='Country Spanish Name')
    name_en = models.CharField(max_length=200, default='', verbose_name='Country English Name')
    description_en = models.TextField(max_length=3000, blank=True)
    description_es = models.TextField(max_length=3000, blank=True)
    recommend = models.PositiveSmallIntegerField(default=0, verbose_name='travellers recommend')
    currency_code = models.CharField(max_length=3, blank=True, verbose_name='Currency Code')
    currency_name = models.CharField(max_length=200, blank=True, verbose_name='Currency Name')
    photo = models.TextField(max_length=5000, default='', blank=True, verbose_name='Country Photo')
    thumbnail = models.TextField(max_length=5000, default='', blank=True, verbose_name='Country Thumbnail')
    capital = models.CharField(max_length=200, blank=True, verbose_name='Capital city')
    zone = models.CharField(max_length=300, blank=True, verbose_name='Country zone',
                            help_text='Look at country_zone.json on json_example folder (client project)')
    active = models.BooleanField(default=False, verbose_name='Active')
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_en

    def get_absolute_url(self):
        return 'page/country/' + self.alias_country

    def get_full_absolute_url(self):
        domain = Site.objects.get_current().domain

        return 'https://%s%s' % (domain, self.get_absolute_url())

    class Meta:
        ordering = ['-created_at']
