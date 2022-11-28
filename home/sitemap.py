from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class homeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)