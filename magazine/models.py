from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class NewsArticle(models.Model):
    pass


class Idea(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    content = models.TextField(_("Content"))

    class Meta:
        verbose_name = _("Idea")
        verbose_name_plural = _("Ideas")

    def __str__(self):
        return self.title

    def get_url_path(self):
        return reverse("idea_details", kwargs={"idea_id": str(self.pk)})

    def get_absolute_url(self):
        pass
