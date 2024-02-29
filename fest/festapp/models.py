from django.db import models

class ExternalUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    college_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    roll = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)  # used as user_name later on
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
