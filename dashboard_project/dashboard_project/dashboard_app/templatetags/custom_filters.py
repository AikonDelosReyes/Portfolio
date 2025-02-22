from django import template

register = template.Library()

@register.filter
def currency_format(value):
    """Format the number as currency with commas and a dollar sign"""
    try:
        value = int(value)
        return "${:,.0f}".format(value)
    except (ValueError, TypeError):
        return value
