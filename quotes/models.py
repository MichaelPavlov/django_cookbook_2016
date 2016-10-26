from django.db import models
from django.db.models import ImageField, CharField, TextField


class InspirationalQuote(models.Model):
    picture = ImageField()
    author = CharField(max_length=250)
    quote = TextField()