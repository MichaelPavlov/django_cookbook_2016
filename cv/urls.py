from django.conf.urls import url

from cv.views import download_cv_pdf

urlpatterns = [
    url(r'^(?P<cv_id>\d+)/pdf/$', download_cv_pdf, name="download_cv_pdf")
]
