# -*- coding: UTF-8 -*-
from django.shortcuts import render

from movies.forms import MovieFilterForm
from movies.models import Movie, Genre, Director, RATING_CHOICES, Actor


def movie_list(request):
    qs = Movie.objects.order_by("title")
    form = MovieFilterForm(data=request.GET)

    facets = {
        "selected": {},
        "categories": {
            "genres": Genre.objects.all(),
            "directors": Director.objects.all(),
            "actors": Actor.objects.all(),
            "ratings": RATING_CHOICES,
        }
    }

    if form.is_valid():
        genre = form.cleaned_data['genre']
        if genre:
            facets["selected"]["genre"] = genre
            qs.filter(genres=genre).distinct()

        director = form.cleaned_data['director']
        if director:
            facets["selected"]["director"] = director
            qs.filter(directors=director).distinct()

        actor = form.cleaned_data['actor']
        if actor:
            facets["selected"]["actor"] = actor
            qs.filter(actors=actor).distinct()

        rating = form.cleaned_data['rating']
        if rating:
            rating = int(rating)
            facets["selected"]["rating"] = (rating, dict(RATING_CHOICES)[rating])
            qs.filter(rating=rating).distinct()

        context = {
            "form": form,
            "facets": facets,
            "object_list": qs
        }

        return render(request, "movies/movie_list.html", context)
