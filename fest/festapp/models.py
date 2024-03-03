from django.db import models
from django.contrib.auth.models import User

class ExternalUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    college_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    roll = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Volunteer(models.Model):
    id = models.AutoField(primary_key=True)
    volunteer_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Organizer(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.OneToOneField('Event', on_delete=models.CASCADE, related_name='organizer', related_query_name='organizer', null=True, blank=True)  # Each organizer can have only one event
    event_date = models.DateField()
    event_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)  # Jury's name
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_date = models.DateField()
    event_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='event_thumbnails/', null=True, blank=True)
    winning_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_events')  # Nullable until the winner is decided

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ['-event_date']

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} registered for {self.event.event_name}"

class Winner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='won_positions')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='winners')
    position = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} - Winner of {self.event.event_name} (Position: {self.position})'
