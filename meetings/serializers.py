from .models import Rooms, Meeting
from rest_framework import serializers

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['id', 'name','capacity','has_projector','has_video_conferencing','has_whiteboard','has_smart_board','has_sound_system','internet_speed_mbps','room_layout','temperature_control','lighting_control','has_refreshments'] 

class MeetingSerializer(serializers.ModelSerializer):
    room = RoomsSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(queryset=Rooms.objects.all(), source='room', write_only=True) #formatted_duration = serializers.SerializerMethodField()
    class Meta:
        model = Meeting
        fields = ['id', 'Title', 'Date', 'start_time', 'Duration', 'room_id', 'room'] 
        extra_kwargs = {
            'duration': {'help_text': "Duration of booking in hours"}
        }
    def validate(self, data):
        """
         Custom validation to check for meeting overlap in the same room.
        """
        room = data.get('room')
        date = data.get('date')
        start_time = data.get('start_time')

        if room and date and start_time:
            overlapping_meetings = Meeting.objects.filter(
                room=room, date=date, start_time=start_time
            )
            if overlapping_meetings.exists():
                raise serializers.ValidationError(
                    "There is already a meeting scheduled in this room at the specified time."
                )       
        return data
    
       # fields = ['id', 'Title', 'Date', 'start_time', 'Duration', 'room_id', 'room', 'formatted_duration'] 

            
       #def get_formatted_duration(self, obj):
           # if obj.duration:
            #    total_seconds = int(obj.duration.total_seconds())
             #   hours, remainder = divmod(total_seconds, 3600)
              #  minutes, _ = divmod(remainder, 60)
               # return f"{hours} hours {minutes} minutes"
            #return "0 hours 0 minutes" '''