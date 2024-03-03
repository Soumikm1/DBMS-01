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
    # student_name = models.CharField(max_length=100)  # used as user_name later on
    department = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Volunteer(models.Model):
    id = models.AutoField(primary_key=True)
    volunteer_name = models.CharField(max_length=100)  # used as user_name
    password = models.CharField(max_length=100)

class Organizer(models.Model):
    id = models.AutoField(primary_key=True)
    event_date = models.DateField()
    event_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)  # jury's name
    password = models.CharField(max_length=100)



# Event model 

# class Event(models.Model):
#     id = models.AutoField(primary_key=True)
#     event_date = models.DateField()
#     event_name = models.CharField(max_length=100)
#     event_type = models.CharField(max_length=100)
#     thumbnail = models.ImageField(upload_to='event_thumbnails/', null=True, blank=True)

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_date = models.DateField()
    event_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='event_thumbnails/', null=True, blank=True)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} - Winner of {self.event.event_name} (Position: {self.position})'