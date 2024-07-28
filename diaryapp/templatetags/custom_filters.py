import base64
from django import template

register = template.Library()

@register.filter
def base64encode(value):
    return base64.b64encode(value).decode('utf-8')

@register.filter
def range_filter(value):
    return range(value)