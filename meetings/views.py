from rest_framework import viewsets
from .models import Rooms, Meeting
from .serializers import RoomsSerializer, MeetingSerializer
from django.shortcuts import render

class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = {
            "message": "Room created successfully!",
            "room": serializer.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
        

class MeetingViewSet(viewsets.ModelViewSet):
   queryset = Meeting.objects.all()
   serializer_class = MeetingSerializer

   def perform_create(self, serializer):
        serializer.save()

   def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = {
            "message": "Meeting created successfully!",
            "meeting": serializer.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

   def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
   def api_interface(request):
    return render(request, 'api_interface.html')
