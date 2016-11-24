# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from locations.models import Location


def location_detail_popup(request, slug):
    location = get_object_or_404(Location, slug=slug)
    return render(request, "locations/location_detail_popup.html", {"location": location})


class LocationDetailView(DetailView):
    model = Location


class LocationListView(ListView):
    model = Location
