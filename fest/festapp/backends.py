from .models import ExternalUser, Student, Volunteer, Organizer

def authenticate_external_user(username, password):
    try:
        user = ExternalUser.objects.get(user_name=username, password=password)
        return user
    except ExternalUser.DoesNotExist:
        return None

def authenticate_student(username, password):
    try:
        student = Student.objects.get(student_name=username, password=password)
        return student
    except Student.DoesNotExist:
        return None

def authenticate_volunteer(username, password):
    try:
        volunteer = Volunteer.objects.get(volunteer_name=username, password=password)
        return volunteer
    except Volunteer.DoesNotExist:
        return None

def authenticate_organizer(username, password):
    try:
        organizer = Organizer.objects.get(user_name=username, password=password)
        return organizer
    except Organizer.DoesNotExist:
        return None
