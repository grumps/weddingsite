from mezzanine_events.models import Event
from datetime import date
from django import template
register = template.Library()

@register.assignment_tag
def countdown():
    """
    Returns countdown to date
    :return: countdown to wedding date of first mezzanine event
    """
    wedding_date = Event.objects.order_by('date')[:1].get()
    countdown_to = abs((wedding_date.date - date.today()).days)
    return countdown_to
