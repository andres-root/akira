from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from agents.main import test

# Create your views here.


class IndexViewset(APIView):
    def get(self, request):
        data = {
            "message": test(),
        }
        return Response(data, status=status.HTTP_200_OK)
