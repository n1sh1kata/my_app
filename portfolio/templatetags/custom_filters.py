from django import template

register = template.Library()

# Bonus (10 points): Create a custom filter to format the count (e.g. $12,450)

@register.filter
def format_count(value):
    try:
        return "${:,.0f}".format(float(value))
    except (ValueError, TypeError):
        return value