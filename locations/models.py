from django.contrib.gis.db import models

from utils.models import upload_to


class Location(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    small_image = models.ImageField(upload_to=upload_to)
    medium_image = models.ImageField(upload_to=upload_to)
    large_image = models.ImageField(upload_to=upload_to)
    point = models.PointField()

    def __str__(self):
        return self.title
