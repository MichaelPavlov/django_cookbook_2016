from crispy_forms import bootstrap
from crispy_forms import layout
from crispy_forms.helper import FormHelper
from django import forms
from django.utils.translation import ugettext_lazy as _

from bulletin_board.models import Bulletin


class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = ["bulletin_type", "title", "description", "contact_person", "phone", "email", "image"]

    def __init__(self, *args, **kwargs):
        super(BulletinForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"

        self.fields["bulletin_type"].widget = forms.RadioSelect()

        # delete empty choice for the type
        del self.fields["bulletin_type"].choices[0]

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Main data"),
                layout.Field("bulletin_type"),
                layout.Field("title", css_class="input-block-level"),
                layout.Field("description", css_class="input-blocklevel", rows=3),
            ),
            layout.Fieldset(
                _("Image"),
                layout.Field("image", css_class="input-block-level"),
                layout.HTML(
                    u"""
                    {% load i18n%}
                    <p class="help-block">
                        {% trans "Available formats are JPG, GIF, PNG. Minimal size is 800 x 800 px." %}
                    </p>
                    """
                ),
                title=_("Image upload"),
                css_id="image_fieldset",
            ),
            layout.Fieldset(
                _("Contact"),
                layout.Field("contact_person", css_class="input-blocklevel"),
                layout.Div(
                    bootstrap.PrependedText("phone", """<span class="glyphicon glyphicon-earphone"></span>""",
                                            css_class="input-blocklevel"),
                    bootstrap.PrependedText("email", "@", css_class="input-block-level",
                                            placeholder="contact@example.com"),
                    css_id="contact_info",
                ),
            ),
            bootstrap.FormActions(
                layout.Submit("submit", _("Save"))
            )
        )
