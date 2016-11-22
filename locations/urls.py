from django.conf.urls import url

from locations.views import LocationDetailView, LocationListView

urlpatterns = [

    url(r'^(?P<pk>\d+)/$', LocationDetailView.as_view(), name="locations-detail"),
    url(r'$', LocationListView.as_view(), name="locations-list"),
]
