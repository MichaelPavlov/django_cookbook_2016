# -*- coding: UTF-8 -*-
from django.db import models
from django.urls import NoReverseMatch
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.fields import MultilingualCharField, MultilingualTextField
from utils.models import UrlMixin


class Category(models.Model):
    title = MultilingualCharField(_("Title"), max_length=200)

    class Meta:
        verbose_name = _("Idea Category")
        verbose_name_plural = _("Idea Categories")

    def __str__(self):
        return self.title


class Idea(UrlMixin):
    title = MultilingualCharField(_("Title"), max_length=200)
    subtitle = MultilingualCharField(_("Subtitle"), max_length=200, blank=True)
    description = MultilingualTextField(_("Description"), blank=True)
    is_original = models.BooleanField(_("Original"))
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"), blank=True, related_name="ideas")

    class Meta:
        verbose_name = _("Idea")
        verbose_name_plural = _("Ideas")

    def __str__(self):
        return self.title

    def get_url_path(self):
        try:
            return reverse("idea_detail", kwargs={"id", self.pk})
        except NoReverseMatch:
            return ""
