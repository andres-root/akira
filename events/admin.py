from django.contrib import admin

from events.models import Event, ScheduleRequest

admin.site.register(Event)
admin.site.register(ScheduleRequest)
