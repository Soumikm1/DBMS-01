from django.contrib import admin
from django.urls import path, include
from fest import views

admin.site.site_header = "FEsT Admin"
admin.site.site_title = "FEsT Admin Portal"
admin.site.index_title = "Welcome to FEsT Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
]
