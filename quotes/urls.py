from django.conf.urls import url

from quotes.views import download_quote_picture, ajax_uploader, add_quote

urlpatterns = [
    url(r'^(?P<quote_id>\d+)/download/$', download_quote_picture, name='download_quote_picture'),
    url(r'^ajax-upload/$', ajax_uploader, name='ajax-uploader'),
    url(r'^add-quote/$', add_quote, name='add-quote'),
]
