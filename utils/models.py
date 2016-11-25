from urllib.parse import urlparse, urlunparse

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import FieldError
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


def upload_to(instance, filename):
    return "%s/%s" % (instance._meta.app_label, filename)


def object_relation_mixin_factory(prefix=None, prefix_verbose=None, add_related_name=False,
                                  limit_content_type_choices_to={}, limit_object_choices_to={}, is_required=False):
    """
    Genrates mixin class for generic foreign keys with dynamic field names.
    The model fields are created like this:

    <<prefix>>_content_type : Field name for "content type"

    <<prefix>>_object_id : Field name for "object id"

    <<prefix>>_content_object : Field name for "content object"

    :param prefix: a prefix which is added in front of the fields
    :param prefix_verbose: a verbose name of the prefix, used generate a title for the field column of the content object in the Admin
    :param add_related_name: a boolean value indicating, that a related name for the generated content type foreign key should be added.
                            This value should be true, if you use more than one ObjectRelateionMixin in your model.
    :param limit_content_type_choices_to:
    :param limit_object_choices_to:
    :param is_required:
    :return: A mixin class for generic foreign keys using "Content type - object id" with dynamic field names.
    """

    p = ""
    if prefix:
        p = "%s_" % prefix

    content_type_field = "%scontent_type" % p
    object_id_field = "%sobject_id" % p
    content_object_field = "%scontent_object" % p

    class TheClass(models.Model):
        class Meta:
            abstract = True

    if add_related_name:
        if not prefix:
            raise FieldError("if add_related_name is set to True, a prefix must be given.")
        related_name = prefix
    else:
        related_name = None

    optional = not is_required
    ct_verbose_name = (
        _("%s's type (model)") % prefix_verbose if prefix_verbose else _("Related object's type (model)")
    )

    content_type = models.ForeignKey(
        ContentType,
        verbose_name=ct_verbose_name,
        related_name=related_name,
        blank=optional,
        null=optional,
        help_text=_("Please select the type (model) for the relation, you want to build."),
        limit_choices_to=limit_content_type_choices_to
    )

    fk_verbose_name = (prefix_verbose or _("Related object"))

    object_id = models.CharField(
        fk_verbose_name,
        blank=optional,
        null=False,
        help_text=_("Please enter the ID of the related object."),
        max_length=255,
        default="",  # for south migrations
    )

    object_id.limit_choices_to = limit_object_choices_to
    # can be retrieved by
    # MyModel._meta.get_field("object_id").limit_choices_to

    content_object = GenericForeignKey(
        ct_field=content_type_field,
        fk_field=object_id_field
    )

    TheClass.add_to_class(content_type_field, content_type)
    TheClass.add_to_class(object_id_field, object_id)
    TheClass.add_to_class(content_object_field, content_object)

    return TheClass


class CreationModificationDateMixin(models.Model):
    """
    Abstract base class with a creation and modification date and time
    """
    created = models.DateTimeField(_("Creation date and time"), editable=False)
    modified = models.DateTimeField(_("Modification date and time"), null=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created = timezone.now()
        else:
            # To ensure that we have a creation data always, we add this one
            if not self.created:
                self.created = timezone.now()
            self.modified = timezone.now()

            super(CreationModificationDateMixin, self).save(*args, **kwargs)

    save.alters_data = True


class UrlMixin(models.Model):
    """
    A replacement for get_absolute_url(). Models extending this mixin should have either get_url or get_url_path implemented
    """

    class Meta:
        abstract = True

    def get_url(self):
        if hasattr(self.get_url_path, "dont_recurse"):
            raise NotImplementedError
        try:
            path = self.get_url_path()
        except NotImplementedError:
            raise
        website_url = getattr(
            settings, "DEFAULT_WEBSITE_URL", "http://127.0.0.1:8000"
        )
        return website_url + path

    get_url.dont_recurse = True

    def get_url_path(self):
        if hasattr(self.get_url, "dont_recurse"):
            raise NotImplementedError
        try:
            url = self.get_url()
        except NotImplementedError:
            raise

        bits = urlparse(url)
        return urlunparse(("", "") + bits[2:])

    get_url_path.dont_recurse = True

    def get_absolute_url(self):
        return self.get_url_path()
