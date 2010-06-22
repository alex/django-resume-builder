from django import template

register = template.Library()

@register.filter
def sort_by_order(value):
    return sorted(value, key=lambda o: o['grouper'].order)

@register.filter("sorted")
def sorted_tag(value, attr):
    return sorted(value, key=lambda o: getattr(o, attr))
