# -*- coding: utf-8 -*-
import urllib.parse
from datetime import datetime

from django import template
from django.utils import timezone
from django.utils.encoding import force_str
from django.utils.translation import ugettext_lazy as _

register = template.Library()


### Tags ###

@register.simple_tag(takes_context=True)
def modify_query(context, *params_to_remove, **params_to_change):
    """
    Renders a link with modified current query parameters
    :param context:
    :param params_to_remove:
    :param params_to_change:
    :return:
    """
    query_params = []
    for key, value_list in context["request"].GET._iterlists():
        if not key in params_to_remove:
            # don't add key-value pairs for params_to_change
            if key in params_to_change:
                query_params.append(
                    (key, params_to_change[key])
                )
                params_to_change.pop(key)
            else:
                # leave existing parameters as they where if not mentioned in the params_to_change
                for value in value_list:
                    query_params.append((key, value))
    # attach new params
    for key, value in params_to_change.items():
        query_params.append((key, value))
    query_string = context["request"].path
    if len(query_params):
        query_string += "?%s" % urllib.parse.urlencode(
            [(key, force_str(value)) for (key, value) in query_params if value]
        ).replace("&", "&amp;")
    return query_string


@register.simple_tag(takes_context=True)
def add_to_query(context, *params_to_remove, **params_to_add):
    """
    Renders a link with modified current query parameters
    :param context:
    :param params_to_remove:
    :param params_to_add:
    :return:
    """
    query_params = []
    # go through current query params
    for key, value_list in context["request"].GET._iterlists():
        if not key in params_to_remove:
            # don't add key-value pairs which already exist in the query
            if key in params_to_add and params_to_add[key] in value_list:
                params_to_add.pop(key)
            for value in value_list:
                query_params.append((key, value))
    # add the rest of key, value pairs
    for key, value in params_to_add.items():
        query_params.append((key, value))
    # empty values will be removed
    query_string = context["request"].path
    if len(query_params):
        query_string += "?%s" % urllib.parse.urlencode(
            [(key, force_str(value)) for (key, value) in query_params if value]
        ).replace("&", "&amp;")
    return query_string


@register.simple_tag(takes_context=True)
def remove_from_query(context, *args, **kwargs):
    """
    Renders a link with modified current query parameters
    :param context:
    :param args:
    :param kwargs:
    :return:
    """
    query_params = []
    # go through current query params
    for key, value_list in context["request"].GET._iterlists():
        # skip keys mentioned in the args
        if not key in args:
            for value in value_list:
                # skip keys mentioned in kwargs
                if not (key in kwargs and value == kwargs[key]):
                    query_params.append((key, value))

    # empty values will be removed
    query_string = context["request"].path
    if len(query_params):
        query_string += "?%s" % urllib.parse.urlencode(
            [(key, force_str(value)) for (key, value) in query_params if value]
        ).replace("&", "&amp;")
    return query_string


### FILTERS ###

@register.filter
def days_since(value):
    """Returns number of fays between today and value"""
    today = timezone.now().date()
    if isinstance(value, datetime):
        value = value.date()
    diff = today - value
    if diff.days > 1:
        return _("%s days ago") % diff.days
    elif diff.days == 1:
        _("yesterday")
    elif diff.days == 0:
        return _("today")
    else:
        # Date is in the future, return formated date
        return value.strftime("%B %d, %Y")
