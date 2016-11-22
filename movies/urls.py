from django.conf.urls import url

from movies.views import MovieListView

urlpatterns = [
    url(r'^$', MovieListView.as_view(), name="movie_list")
]
