# from django.contrib import admin
from django.urls import path
from festapp import views
from festapp.views import event_detail, register_event, create_event

urlpatterns = [
    path('', views.home, name='home'),
    path('home/<str:type>/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('register_event/<int:event_id>/', register_event, name='register_event'),

    path('create_event/', create_event, name='create_event'),

    path('external_login/', views.external_login, name='external_login'),
    path('student_login/', views.student_login, name='student_login'),
    path('volunteer_login/', views.volunteer_login,name='volunteer_login'),
    path('organizer_login/', views.organizer_login, name='organizer_login'),
    path('organizer_dashboard/', views.organizer_dashboard, name='organizer_dashboard'),
]

