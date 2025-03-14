import datetime
from django import template

register = template.Library()


@register.simple_tag
def current_timess(format_string):
    return datetime.datetime.now().strftime(format_string)
