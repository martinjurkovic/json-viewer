from django import template

register = template.Library()

@register.filter
def split_by_underscore(value):
    return ' ' .join([w.capitalize() for w in value.split('_')])
