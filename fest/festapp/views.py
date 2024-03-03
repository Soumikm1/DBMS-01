from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from festapp.models import ExternalUser, Student, Volunteer, Organizer ,Event , Registration
# from datetime import datetime
from festapp.backends import authenticate_student, authenticate_volunteer, authenticate_organizer, authenticate_external_user
# @login_required(login_url='/login')
# def home(request):
#     return render(request, 'home.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventCreationForm
from .models import Organizer



@login_required(login_url='/login')
def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})


@login_required
def register_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    user = request.user

    if Registration.objects.filter(user=user, event=event).exists():
        messages.warning(request, 'You are already registered for this event.')
    else:
        Registration.objects.create(user=user, event=event)
        messages.success(request, 'Successfully registered for the event.')

    return redirect('event_detail', event_id=event.id)

@login_required(login_url='/login')
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html', {'event': event})


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
        print(user_name)
        print(password)
        user = authenticate_external_user(user_name, password)
        if user is not None:
            user = authenticate(username = user_name, password = password)
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
        if user is not None:
            user = authenticate(username = user_name, password = password)
            login(request, user)
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
        print(user_name)
        print(password)
        user = authenticate_volunteer(user_name, password)
        print(user)
        if user is not None:
            user = authenticate(username = user_name, password = password)
            login(request, user)
            return redirect('volunteer_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    elif request.method == 'GET':
        return render(request, 'volunteer_login.html')
    else:
        return render(request, 'login.html')

from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect, messages

def organizer_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            login(request, user)
            return redirect('organizer_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('/')
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
        email = request.POST.get('email')
        
        # Create a new ExternalUser instance
        new_external_user = ExternalUser(
            name=name,
            college_id=college_id,
            user_name=user_name,
            password=password
        )
        print("saving new user")
        # Save the new ExternalUser instance
        new_external_user.save()
        print("New User " + name + "saved")
        create_default_user(user_name, email, password)
        # Redirect to the login page
        return redirect('login')
    elif request.method == 'GET':
        return render(request, 'signup.html')
    return render(request, 'signup.html')



# @login_required(login_url='/login')
# def organizer_dashboard(request):
#     return render(request, 'organizer_dashboard.html')


# views.py
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventCreationForm

from django.shortcuts import render, redirect
from .models import Event
from .forms import EventCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import EventCreationForm
from .models import Organizer

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from .forms import EventCreationForm
from .models import Organizer

@login_required(login_url='/login')
def create_event(request):
    # Ensure the user is an organizer

    if not Organizer.objects.filter(user_name=request.user).exists():
        return HttpResponse("You don't have permission to access this page.")

    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            # Save the event with organizers in a single step
            event = form.save(commit=False)
            event.user = request.user  # Assign current user as organizer
            event.save()  # Save the event and related fields

            # Alternative approach (if the user can belong to multiple organizers)
            # organizers = Organizer.objects.filter(user=request.user)  # Get organizers for the user
            # event.organizers.set(organizers)  # Add organizers to the event

            return HttpResponse('Event created successfully')
    else:
        form = EventCreationForm()

    return render(request, 'create_event.html', {'form': form})

from django.shortcuts import render


# Separate dashboard views for different user types
@login_required(login_url='/login')
def external_dashboard(request):
    return render(request, 'external_dashboard.html')

@login_required(login_url='/login')
def student_dashboard(request):
    if request.method == 'POST':
        # Check if the request is coming from the Logout button
        print("POST incoming")
        if 'logout' in request.POST:
            # Perform logout actions here, such as clearing session data or redirecting to a logout page
            # For example, you can clear session data and redirect to the login page
            # Example: request.session.flush() to clear session data
            # Then redirect to the login page
            request.session.flush()
            print("Cleanup for logout")
            logout(request)
            print("logged out")
            return redirect('login')  # Assuming 'login' is the URL name for the login page
        # else: return render(request, 'student_dashboard.html')
    return render(request, 'student_dashboard.html')

@login_required(login_url='/login')
def volunteer_dashboard(request):
    return render(request, 'volunteer_dashboard.html')


def organizer_dashboard(request):
    # Your logic for the organizer dashboard goes here
    return render(request, 'organizer_dashboard.html')

# @login_required(login_url='/login')
# def organizer_dashboard(request):
#     if request.method == 'POST':
#         form = EventCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             event = form.save()(commit=False)
            
#             # Get the organizer
#             organizers = Organizer.objects.filter(user_name=request.user.username)
#             event.save()  # Now we can save the event to generate its ID
#             event.organizers.set(organizers)
            
#             # Associate the event with the organizer

#             event.save()

#             return redirect('organizer_dashboard')
#     else:
#         form = EventCreationForm()

#     return render(request, 'organizer_dashboard.html', {'form': form})



def create_default_user(username, email, password):
    user = User.objects.create_user(username=username, email=email, password=password)
    return user