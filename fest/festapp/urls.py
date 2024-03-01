# from django.contrib import admin
from django.urls import path
from festapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('external_login/', views.external_login, name='external_login'),
    path('student_login/', views.student_login, name='student_login'),
    path('volunteer_login/', views.volunteer_login,name='volunteer_login'),
    path('organizer_login/', views.organizer_login, name='organizer_login'),
    path('external_dashboard/', views.external_dashboard, name='external_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('volunteer_dashboard/', views.volunteer_dashboard, name='volunteer_dashboard'),
    path('organizer_dashboard/', views.organizer_dashboard, name='organizer_dashboard'),
]

