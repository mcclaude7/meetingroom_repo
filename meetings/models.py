from django.db import models

class Rooms(models.Model):
    name = models.CharField(max_length=300, unique=True)
    capacity = models.PositiveIntegerField(default=10,help_text="Maximum number of people the room can accommodate")
    has_projector = models.BooleanField(default=False)
    has_video_conferencing = models.BooleanField(default=False)
    has_whiteboard = models.BooleanField(default=True)
    has_smart_board = models.BooleanField(default=False)
    has_sound_system = models.BooleanField(default=False)
    internet_speed_mbps = models.PositiveIntegerField(null=True, blank=True, help_text="Internet speed in Mbps")
    room_layout = models.CharField(
        max_length=50,
        choices=[('round_table', 'Round Table'), ('conference', 'Conference Table'), ('informal', 'Informal Seating')],
        default='conference'
    )
    temperature_control = models.BooleanField(default=True)
    lighting_control = models.BooleanField(default=True)
    has_refreshments = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Meeting(models.Model):
    Title = models.CharField(max_length=250)
    Date = models.DateField()
    start_time = models.TimeField()
    Duration = models.DurationField(help_text="Duration of booking in Hrs")
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='Meeting')

#def formatted_duration(self):
 #       if self.Duration:
  #          total_seconds = int(self.Duration.total_seconds())
   #         hours, remainder = divmod(total_seconds, 3600)
    #        minutes, _ = divmod(remainder, 60)
     #       return f"{hours} hours {minutes} minutes"
      #  return "0 hours 0 minutes"