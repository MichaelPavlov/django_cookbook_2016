from django.conf.urls import url

from locations.views import LocationDetailView, LocationListView, location_detail_popup

urlpatterns = [
    url(r'^$', LocationListView.as_view(), name="locations-list"),
    url(r'^(?P<slug>[^/]+)/popup/$', location_detail_popup, name="location-detail-popup"),
    url(r'^(?P<slug>[^/]+)/$', LocationDetailView.as_view(), name="location-detail"),

]
