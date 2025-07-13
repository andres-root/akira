from rest_framework import serializers

from events.models import Event, ScheduleRequest


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class ScheduleRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleRequest
        fields = "__all__"
