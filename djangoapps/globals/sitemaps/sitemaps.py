from django.contrib.sitemaps import Sitemap

from djangoapps.schools.models import School
from djangoapps.countries.models import Country


class SchoolSitemap(Sitemap):
    changefreq = "daily"
    priority = 1
    protocol = "http"

    def items(self):
        return School.objects.filter(active=True)

    def lastmod(self, item):
        return item.updated_at


class CountrySitemap(Sitemap):
    changefreq = "daily"
    priority = 1
    protocol = "http"

    def items(self):
        return Country.objects.filter(active=True)

    def lastmod(self, item):
        return item.updated_at