from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from festapp.models import ExternalUser, Student, Volunteer, Organizer
# from datetime import datetime

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
        
        # Authenticate user
        user = authenticate(request, user_name=user_name, password=password, user_type='external')
        
        # Check if authentication was successful
        if user is not None:
            # If user is authenticated, log them in
            login(request, user)
            # Redirect to student dashboard or any desired page
            return redirect('external_dashboard')
        else:
            # If authentication failed, display error message
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # Redirect back to login page with error message
    else:
        # If request method is not POST, render the login page
        return render(request, 'login.html')

def student_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, user_name=user_name, password=password, user_type='student')
        
        # Check if authentication was successful
        if user is not None:
            # If user is authenticated, log them in
            login(request, user)
            # Redirect to student dashboard or any desired page
            return redirect('student_dashboard')
        else:
            # If authentication failed, display error message
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # Redirect back to login page with error message
    else:
        # If request method is not POST, render the login page
        return render(request, 'login.html')

def volunteer_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, user_name=user_name, password=password, user_type='volunteer')
        
        # Check if authentication was successful
        if user is not None:
            # If user is authenticated, log them in
            login(request, user)
            # Redirect to student dashboard or any desired page
            return redirect('volunteer_dashboard')
        else:
            # If authentication failed, display error message
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # Redirect back to login page with error message
    else:
        # If request method is not POST, render the login page
        return render(request, 'login.html')

def organizer_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, user_name=user_name, password=password, user_type='organizer')
        
        # Check if authentication was successful
        if user is not None:
            # If user is authenticated, log them in
            login(request, user)
            # Redirect to student dashboard or any desired page
            return redirect('organizer_dashboard')
        else:
            # If authentication failed, display error message
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # Redirect back to login page with error message
    else:
        # If request method is not POST, render the login page
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
    # Logic for external user dashboard
    pass

@login_required(login_url='/login')
def student_dashboard(request):
    # Logic for student dashboard
    pass

@login_required(login_url='/login')
def volunteer_dashboard(request):
    # Logic for volunteer dashboard
    pass

@login_required(login_url='/login')
def organizer_dashboard(request):
    # Logic for organizer dashboard
    pass
