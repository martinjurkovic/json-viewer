from django import template

register = template.Library()

@register.filter
def split_by_underscore(value):
    return ' ' .join([w.capitalize() for w in value.split('_')])

@register.filter
def is_in_range(value, arg):
    # Ensure arg is a list of two values representing the range
    if len(arg) != 2:
        return False
    try:
        lower_bound, upper_bound = float(arg[0]), float(arg[1])
        return lower_bound <= value <= upper_bound
    except (ValueError, TypeError):
        return False