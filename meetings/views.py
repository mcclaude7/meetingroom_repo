from rest_framework import viewsets
from .models import Rooms, Meeting
from .serializers import RoomsSerializer, MeetingSerializer

class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
