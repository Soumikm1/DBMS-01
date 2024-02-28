from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from festapp.models import Item_List
from datetime import datetime

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        # Assuming signup form fields are posted here
        # You can create a new user for external participants
        # Ensure appropriate form validation and user creation process
        # Example:
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # email = request.POST.get('email')
        # user = User.objects.create_user(username=username, email=email, password=password)
        # user.groups.add(Group.objects.get(name='External Participants'))
        return redirect('login')
    return render(request, 'signup.html')