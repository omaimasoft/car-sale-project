from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Car

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = "daily"

    def items(self):
        return ['home', 'car_list']

    def location(self, item):
        return reverse(item)


class CarSitemap(Sitemap):
    priority = 0.8
    changefreq = "daily"

    def items(self):
        return Car.objects.all()
