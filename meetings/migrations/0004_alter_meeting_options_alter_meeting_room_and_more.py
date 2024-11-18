# Generated by Django 5.0.7 on 2024-11-04 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_alter_meeting_duration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'ordering': ['Date']},
        ),
        migrations.AlterField(
            model_name='meeting',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='meetings.rooms'),
        ),
        migrations.AlterUniqueTogether(
            name='meeting',
            unique_together={('room', 'Date', 'start_time')},
        ),
    ]