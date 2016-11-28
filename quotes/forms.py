import os

from crispy_forms import bootstrap
from crispy_forms import layout
from crispy_forms.helper import FormHelper
from django import forms
from django.conf import settings
from django.core.files import File
from django.utils.translation import ugettext_lazy as _

from quotes.models import InspirationalQuote


class InspirationalQuoteForm(forms.ModelForm):
    picture_path = forms.CharField(
        max_length=255,
        widget=forms.HiddenInput(),
        required=False
    )
    delete_picture = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False
    )

    class Meta:
        model = InspirationalQuote
        fields = ["author", "quote"]

    def __init__(self, *args, **kwargs):
        super(InspirationalQuoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Quote"),
                layout.Field("author"),
                layout.Field("quote", rows=3),
                layout.HTML("""
                    {% include "quotes/includes/image_upload_widget.html" %}
                """),
                layout.Field("picture_path"), #hidden
                layout.Field("delete_picture"), #hidden
            ),
            bootstrap.FormActions(
                layout.Submit("submit", _("Save"), css_class="btn btn-primary")
            )
        )

    def save(self, commit=True):
        instance = super(InspirationalQuoteForm, self).save(commit=commit)

        if self.cleaned_data['delete_picture'] and instance.picture:
            instance.picture.delete()

        if self.cleaned_data['picture_path']:
            tmp_path = self.cleaned_data['picture_path']
            abs_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)

            filename = InspirationalQuote._meta.get_field('picture').upload_to(instance, tmp_path)
            instance.picture.save(
                filename,
                File(open(abs_tmp_path, "rb")),
                False
            )

            os.remove(abs_tmp_path)

        instance.save()
        return instance


