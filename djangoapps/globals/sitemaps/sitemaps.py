from django.contrib.sitemaps import Sitemap

from djangoapps.schools.models import School


class SchoolSitemap(Sitemap):
    changefreq = "daily"
    priority = 1
    protocol = "https"

    def items(self):
        return School.objects.filter(active=True)

    def lastmod(self, item):
        return item.updated_at

