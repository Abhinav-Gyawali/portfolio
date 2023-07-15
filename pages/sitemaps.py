from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'about','services', 'contact','privacy-policy','projects','signup']  # Add the names of your static views here

    def location(self, item):
        return reverse(item)
