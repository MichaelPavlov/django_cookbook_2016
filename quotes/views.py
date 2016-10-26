# -*- coding: UTF-8 -*-
import os

from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from quotes.models import InspirationalQuote


@login_required(login_url="login_page")
def download_quote_picture(request, quote_id):
    quote = get_object_or_404(InspirationalQuote, pk=quote_id)
    file_name, file_extension = os.path.splitext(quote.picture.file.name)
    file_extension = file_extension[1:] # remove the dot
    response = FileResponse(
        quote.picture.file,
        content_type="image/%s" % file_extension
    )
    response["Content-Disposition"] = "attachment; filename=%s---%s.%s" % (
        slugify(quote.author)[:100],
        slugify(quote.quote)[:100],
        file_extension
    )

    return response