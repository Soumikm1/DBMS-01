from django.contrib.auth.backends import BaseBackend
from .models import ExternalUser, Student, Volunteer, Organizer

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, user_type=None):
        # Depending on the user type, authenticate against the appropriate model
        if user_type == 'external':
            try:
                user = ExternalUser.objects.get(user_name=username)
                if user.check_password(password):
                    return user
            except ExternalUser.DoesNotExist:
                return None
        elif user_type == 'student':
            try:
                user = Student.objects.get(student_name=username)
                if user.check_password(password):
                    return user
            except Student.DoesNotExist:
                return None
        elif user_type == 'volunteer':
            try:
                user = Volunteer.objects.get(volunteer_name=username)
                if user.check_password(password):
                    return user
            except Volunteer.DoesNotExist:
                return None
        elif user_type == 'organizer':
            try:
                user = Organizer.objects.get(user_name=username)
                if user.check_password(password):
                    return user
            except Organizer.DoesNotExist:
                return None
        return None
