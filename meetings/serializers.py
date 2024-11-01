from .models import Rooms, Meeting
from rest_framework import serializers

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['id', 'name','capacity','has_projector','has_video_conferencing','has_whiteboard','has_smart_board','has_sound_system','internet_speed_mbps','room_layout','temperature_control','lighting_control','has_refreshments'] 

class MeetingSerializer(serializers.ModelSerializer):
    room = RoomsSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(queryset=Rooms.objects.all(), source='room')
    #formatted_duration = serializers.SerializerMethodField()
    class Meta:
        model = Meeting
        fields = ['id', 'Title', 'Date', 'start_time', 'Duration', 'room_id', 'room'] 
       # fields = ['id', 'Title', 'Date', 'start_time', 'Duration', 'room_id', 'room', 'formatted_duration'] 

            
       #def get_formatted_duration(self, obj):
           # if obj.duration:
            #    total_seconds = int(obj.duration.total_seconds())
             #   hours, remainder = divmod(total_seconds, 3600)
              #  minutes, _ = divmod(remainder, 60)
               # return f"{hours} hours {minutes} minutes"
            #return "0 hours 0 minutes" '''