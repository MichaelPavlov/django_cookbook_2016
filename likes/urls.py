from django.conf.urls import url

from likes.views import json_set_like

urlpatterns = [
    url(r'^(?P<content_type_id>[^/]+)/(?P<object_id>[^/]+)/$', json_set_like, name="json-set-like"),

]
