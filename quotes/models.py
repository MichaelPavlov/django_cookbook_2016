# -*- coding: UTF-8 -*-
import os

from django.conf import settings
from django.db import models
from django.urls import NoReverseMatch
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from utils.models import UrlMixin


def upload_to(instance, filename):
    now = timezone.now()
    filename_base, filename_ext = os.path.splittext(filename)
    return "quotes/%s%s" % (now.strftime("%Y/%m/%Y%m%d%H%M%S"), filename_ext.lower())


class InspirationalQuote(UrlMixin):
    author = models.CharField(_("Author"), max_length=200)
    quote = models.TextField(_("Quote"))
    picture = models.ImageField(_("Picture"), upload_to=upload_to, blank=True, null=True)
    language = models.CharField(_("Language"), max_length=2, blank=True, choices=settings.LANGUAGES)

    class Meta:
        verbose_name = _("Inspirational Quote")
        verbose_name_plural = _("Inspirational Quotes")

    def __str__(self):
        return self.quote

    def get_url_path(self):
        try:
            return reverse("quote_detail", kwargs={"id", self.pk})
        except NoReverseMatch:
            return ""

    def title(self):
        return self.quote

# class InspirationalQuote(models.Model):
#     picture = ImageField()
#     author = CharField(max_length=250)
#     quote = TextField()
