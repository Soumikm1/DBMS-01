from django.contrib import admin
from .models import ExternalUser, Student, Volunteer, Organizer

# Register your models here
admin.site.register(ExternalUser)
admin.site.register(Student)
admin.site.register(Volunteer)
admin.site.register(Organizer)
