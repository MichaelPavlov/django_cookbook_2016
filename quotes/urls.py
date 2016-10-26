from django.conf.urls import url

from quotes.views import download_quote_picture

urlpatterns = [
    url(r'^(?P<quote_id>\d+)/download/$', download_quote_picture, name='download_quote_picture'),
]
