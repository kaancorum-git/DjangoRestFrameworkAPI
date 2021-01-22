from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Events
from .serializers import EventsSerializer
from django.core import serializers
from .models import Sessions
#data = serializers.serialize( "python", Sessions.objects.all() )


# Create your views here.

class EventList(APIView):
    def get(self, request):
        events = Events.objects.all()
        serializer = EventsSerializer(events, many=True)
        return  Response(serializer.data)
    def post(self):
            pass
