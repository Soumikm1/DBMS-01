from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from festapp.models import Item_List
from datetime import datetime

def home(request):
    if request.user.is_authenticated:
        return dashboard(request)
    return render(request, 'home.html')

@login_required(login_url='/login')
def dashboard(request):
    user_type = None
    if request.user.groups.filter(name='External Participants').exists():
        user_type = 'external'
    elif request.user.groups.filter(name='Students').exists():
        user_type = 'student'
    elif request.user.groups.filter(name='Volunteers').exists():
        user_type = 'volunteer'
    elif request.user.groups.filter(name='Organizers/Judges').exists():
        user_type = 'organizer'
    return render(request, 'dashboard.html', {'user_type': user_type})

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
    pass

def student_login(request):
    pass

def volunteer_login(request):
    pass

def organizer_login(request):
    pass

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # Check if username is available
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': 'Username already exists.'})
        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        # Add the new user to the 'External Participants' group
        external_participants_group = Group.objects.get(name='External Participants')
        user.groups.add(external_participants_group)
        # Redirect to login page
        return redirect('login')
    return render(request, 'signup.html')

@login_required(login_url='/login')
def dashboard(request):
    user_type = None
    if request.user.groups.filter(name='External Participants').exists():
        user_type = 'external'
        user_info = ExternalParticipant.objects.get(user=request.user)
    elif request.user.groups.filter(name='Students').exists():
        user_type = 'student'
        user_info = Student.objects.get(user=request.user)
    elif request.user.groups.filter(name='Volunteers').exists():
        user_type = 'volunteer'
        user_info = Volunteer.objects.get(user=request.user)
    elif request.user.groups.filter(name='Organizers/Judges').exists():
        user_type = 'organizer'
        user_info = OrganizerJudge.objects.get(user=request.user)
    return render(request, 'dashboard.html', {'user_type': user_type, 'user_info': user_info})
