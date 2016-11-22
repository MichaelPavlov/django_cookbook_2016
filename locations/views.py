# Create your views here.
from django.views.generic import DetailView, ListView

from locations.models import Location


class LocationDetailView(DetailView):
    model = Location

class LocationListView(ListView):
    model = Location