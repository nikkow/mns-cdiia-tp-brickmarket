from django import template

register = template.Library()

@register.filter
def price_from_cents(value):
  try:
    return int(value) / 100
  except:
    return value