import django.contrib
from mezzanine.pages.admin import PageAdmin
from .models import Event, EventContainer
from copy import deepcopy

# event_admin_fieldsets = deepcopy(PageAdmin.fieldsets)
# event_admin_fieldsets[0][1]["fields"]

class EventAdmin(PageAdmin):
    fieldsets = (
        deepcopy(PageAdmin.fieldsets[0]),
        ("Event details", {
            'fields': (
                'content', 'date', ('start_time', 'end_time'), 'location', 'attire', 'mapbox_id', 'mappable_location', ('lat', 'lon'), 'rsvp')
        }),
        deepcopy(PageAdmin.fieldsets[1]),
    )


django.contrib.admin.site.register(Event, EventAdmin)

django.contrib.admin.site.register(EventContainer, PageAdmin)
