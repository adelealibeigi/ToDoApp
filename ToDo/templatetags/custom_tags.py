from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag
def delta_days(due):
    delta = due.date() - datetime.now().date()
    return delta.days
