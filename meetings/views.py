from rest_framework import viewsets
from .models import Rooms, Meeting
from .serializers import RoomsSerializer, MeetingSerializer
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

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
    

    #def create_room(request):
     #   if request.method == 'POST':
      #       room_name = request.POST.get('name')
       #      serializer = RoomsSerializer(data={'name': room_name})
        #     if serializer.is_valid():
         #        serializer.save()
          #       response = {"message": "Room created successfully!", "room": serializer.data}
           #  else:
            #     response = {"errors": serializer.errors}
             #return render(request, 'api_interface.html', {"room_response": response})
        #return redirect('api_interface')

    
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


 #  def create_meeting(request):
  #  if request.method == 'POST':
   #     meeting_title = request.POST.get('title')
    #    room_id = request.POST.get('room')
     #   serializer = MeetingSerializer(data={'title': meeting_title, 'room': room_id})
      #  if serializer.is_valid():
       #     serializer.save()
        #    response = {"message": "Meeting created successfully!", "meeting": serializer.data}
  #      else:
   #         response = {"errors": serializer.errors}
    #    return render(request, 'api_interface.html', {"meeting_response": response})
    #return redirect('api_interface')


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
    
    
