from django.contrib import admin
from .models import ExternalUser, Student, Volunteer, Organizer , Event,Registration, Winner

# Register your models here
admin.site.register(ExternalUser)
admin.site.register(Student)
admin.site.register(Volunteer)
admin.site.register(Organizer)

admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(Winner)