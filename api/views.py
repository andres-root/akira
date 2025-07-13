from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from agents.calendar_agent import CalendarAgent
from events.models import Event, ScheduleRequest
from events.serializers import EventSerializer, ScheduleRequestSerializer

calendar_agent = CalendarAgent()


class IndexViewset(APIView):
    def get(self, request):
        prompt = request.query_params.get("prompt")
        response = calendar_agent.run(prompt)
        parsed_response = response.choices[0].message.parsed
        print(parsed_response)
        print(type(parsed_response))
        return Response(parsed_response.model_dump(), status=status.HTTP_200_OK)


class ScheduleRequestViewset(viewsets.ModelViewSet):
    queryset = ScheduleRequest.objects.all()
    serializer_class = ScheduleRequestSerializer


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
