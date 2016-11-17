# -*- coding: UTF-8 -*-
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from weasyprint import HTML

from cv.models import CV


def download_cv_pdf(request, cv_id):
    cv = get_object_or_404(CV, pk=cv_id)

    html = render_to_string("cv/cv_pdf.html", {
        "cv": cv,
        "MEDIA_ROOT": settings.MEDIA_ROOT,
        "STATIC_ROOT": settings.STATIC_ROOT,
    })
    html = HTML(string=html)
    main_doc = html.render()
    pdf = main_doc.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    # response["Content-Disposition"] = "attachment; filename=%s_%s.pdf" % (cv.first_name, cv.last_name)
    return response
