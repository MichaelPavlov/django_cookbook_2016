# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from movies.models import Genre, Director, Actor, RATING_CHOICES


class MovieFilterForm(forms.Form):
    genre = forms.MultipleChoiceField(
        label=_("Genre"),
        required=False,
        # queryset=Genre.objects.all()
    )

    director = forms.MultipleChoiceField(
        label=_("Director"),
        required=False,
        # queryset=Director.objects.all()
    )

    actor = forms.MultipleChoiceField(
        label=_("Actor"),
        required=False,
        # queryset=Actor.objects.all()
    )

    rating = forms.ChoiceField(
        label=_("Rating"),
        required=False,
        choices=RATING_CHOICES,
    )
