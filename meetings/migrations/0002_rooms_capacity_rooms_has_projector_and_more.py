# Generated by Django 5.0.7 on 2024-11-01 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='capacity',
            field=models.PositiveIntegerField(default=10, help_text='Maximum number of people the room can accommodate'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='has_projector',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rooms',
            name='has_refreshments',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rooms',
            name='has_smart_board',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rooms',
            name='has_sound_system',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rooms',
            name='has_video_conferencing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rooms',
            name='has_whiteboard',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rooms',
            name='internet_speed_mbps',
            field=models.PositiveIntegerField(blank=True, help_text='Internet speed in Mbps', null=True),
        ),
        migrations.AddField(
            model_name='rooms',
            name='lighting_control',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rooms',
            name='room_layout',
            field=models.CharField(choices=[('round_table', 'Round Table'), ('conference', 'Conference Table'), ('informal', 'Informal Seating')], default='conference', max_length=50),
        ),
        migrations.AddField(
            model_name='rooms',
            name='temperature_control',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]