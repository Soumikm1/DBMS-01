from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from datetime import timedelta
from django.conf import settings

# class CustomUser(AbstractUser):
#     # add your custom fields here

#     # Specify related_name for groups and user_permissions
#     groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
#     user_permissions = models.ManyToManyField(
#         Permission, related_name='customuser_set', blank=True
#     )

#     last_login = models.DateTimeField(blank=True, null=True)


#     def __str__(self):
#         return self.username

#     def update_last_login(self, request=None):
#         # Override update_last_login to avoid updating the last_login field
#         if request is not None:
#             if self.last_login is None or self.last_login < timezone.now() - timedelta(seconds=settings.SESSION_COOKIE_AGE):
#                 self.last_login = timezone.now()
#                 self.save(update_fields=['last_login'])

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
    # student_name = models.CharField(max_length=100)  # used as user_name later on
    department = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Volunteer(models.Model):
    id = models.AutoField(primary_key=True)
    volunteer_name = models.CharField(max_length=100)  # used as user_name
    password = models.CharField(max_length=100)

class Organizer(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)  # Jury's name
    password = models.CharField(max_length=100)
    organized_events = models.ManyToManyField('Event', related_name='organizer_events', related_query_name='organizer_event')

    def create_event(self, event_data):
        event = Event.objects.create(**event_data, event_organizer=self)
        return event

    def __str__(self):
        return self.user_name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_date = models.DateField()
    event_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    # thumbnail = models.ImageField(upload_to='event_thumbnails/', null=True, blank=True)
    organizers = models.ManyToManyField(Organizer, related_name='organizer_events', related_query_name='organizer_event', blank=True)
    # event_organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name='created_events', null=True)

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ['-event_date']


    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ['-event_date']



# Event model 

# class Event(models.Model):
#     id = models.AutoField(primary_key=True)
#     event_date = models.DateField()
#     event_name = models.CharField(max_length=100)
#     event_type = models.CharField(max_length=100)
#     thumbnail = models.ImageField(upload_to='event_thumbnails/', null=True, blank=True)

# class Event(models.Model):
#     id = models.AutoField(primary_key=True)
#     event_date = models.DateField()
#     event_name = models.CharField(max_length=100)
#     event_type = models.CharField(max_length=100)
#     thumbnail = models.ImageField(upload_to='event_thumbnails/', null=True, blank=True)
#     organizers = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name='events', default=1)

#     def __str__(self):
#         return self.event_name

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} registered for {self.event.event_name}"

class Winner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} - Winner of {self.event.event_name} (Position: {self.position})'