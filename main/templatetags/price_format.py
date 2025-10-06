from django import template

register = template.Library()


@register.filter
def spaced_price(value):
    try:
        value = int(float(value))
        return f"{value:,}".replace(",", "\u2009")
    except (ValueError, TypeError):
        return ''


@register.filter
def schema_price(value):
    try:
        return f"{float(value):.2f}"
    except (ValueError, TypeError):
        return ''
