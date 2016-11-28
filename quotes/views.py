# -*- coding: UTF-8 -*-
import os

from ajaxuploader.views import AjaxFileUploader
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import slugify

from quotes.forms import InspirationalQuoteForm
from quotes.models import InspirationalQuote

ajax_uploader = AjaxFileUploader()


@login_required(login_url="login_page")
def download_quote_picture(request, quote_id):
    quote = get_object_or_404(InspirationalQuote, pk=quote_id)
    file_name, file_extension = os.path.splitext(quote.picture.file.name)
    file_extension = file_extension[1:]  # remove the dot
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


def add_quote(request):
    if request.method == "POST":
        form = InspirationalQuoteForm(
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            quote = form.save()
            return redirect("add_quote_done")
    else:
        form = InspirationalQuoteForm()
    return render(request, "quotes/change_quote.html", {"form": form})
