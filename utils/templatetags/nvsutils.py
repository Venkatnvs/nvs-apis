from django import template
from django.conf import settings
import os
from django.contrib.sites.shortcuts import get_current_site

register = template.Library()

@register.filter
def replace_v(value, arg):
    if len(arg.split('|')) != 2:
        return value
    what, to = arg.split('|')
    value = value.replace(what, to)
    print(value)
    return value

@register.simple_tag
def replace_request_with_domain(*args, **kwargs):
    value = args[0]
    value = value.replace("<request>",f'http://{get_current_site(args[1]).domain}')
    return value
