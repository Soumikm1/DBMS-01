from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from festapp.models import ExternalUser, Student, Volunteer, Organizer
# from datetime import datetime
from festapp.backends import authenticate_student, authenticate_volunteer, authenticate_organizer, authenticate_external_user

def home(request):
    if request.user.is_authenticated:
        # Redirect directly to the respective dashboard based on user type
        if request.user.groups.filter(name='External Participants').exists():
            return redirect('external_dashboard')
        elif request.user.groups.filter(name='Students').exists():
            return redirect('student_dashboard')
        elif request.user.groups.filter(name='Volunteers').exists():
            return redirect('volunteer_dashboard')
        elif request.user.groups.filter(name='Organizers/Judges').exists():
            return redirect('organizer_dashboard')
    return render(request, 'home.html')

def login_view(request):
    user_type = 'user_type'
    if request.method == 'POST':
        # Assuming you have a dropdown menu with name 'user_type' in your login form
        user_type = request.POST.get('user_type')
        if user_type == 'external':
            return redirect('external_login')
        elif user_type == 'student':
            return redirect('student_login')
        elif user_type == 'volunteer':
            return redirect('volunteer_login')
        elif user_type == 'organizer':
            return redirect('organizer_login')
    return render(request, 'login.html', {'user_type': user_type})

def external_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate_external_user(user_name, password)
        if user is not None:
            login(request, user)
            return redirect('external_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    elif request.method == 'GET':
        return render(request, 'external_login.html')
    else:
        return render(request, 'login.html')

def student_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate_student(user_name, password)
        print(user)
        if user is not None:
            print("Going to dashboard")
            login(request, user)
            print("Going to dashboard1")
            return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    elif request.method == 'GET':
        return render(request, 'student_login.html')
    else:
        return render(request, 'login.html')

def volunteer_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate_volunteer(user_name, password)
        if user is not None:
            login(request, user)
            return redirect('volunteer_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    elif request.method == 'GET':
        return render(request, 'volunteer_login.html')
    else:
        return render(request, 'login.html')

def organizer_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate_organizer(user_name, password)
        if user is not None:
            login(request, user)
            return redirect('organizer_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    elif request.method == 'GET':
        return render(request, 'organizer_login.html')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        college_id = request.POST.get('college_id')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        
        # Create a new ExternalUser instance
        new_external_user = ExternalUser(
            name=name,
            college_id=college_id,
            user_name=user_name,
            password=password
        )
        
        # Save the new ExternalUser instance
        new_external_user.save()
        
        # Redirect to the login page
        return redirect('login')
        
    return render(request, 'signup.html')

# Separate dashboard views for different user types
@login_required(login_url='/login')
def external_dashboard(request):
    return HttpResponse("External Dashboard")

@login_required(login_url='/login')
def student_dashboard(request):
    return HttpResponse("Student Dashboard")

@login_required(login_url='/login')
def volunteer_dashboard(request):
    return HttpResponse("Volunteer Dashboard")

@login_required(login_url='/login')
def organizer_dashboard(request):
    return HttpResponse("organizer Dashboard")
