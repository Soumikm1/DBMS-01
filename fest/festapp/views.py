from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from festapp.models import Item_List
from datetime import datetime

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_pages = {
            'owner': '/',
            'daily_manager': '/reportSale',
            'order_manager': '/viewInventory',
            'sales_manager': '/reportSale',
            'revenue_manager': '/viewGraph',
        }
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/')
            redirect_url = user_pages.get(username, '/')
            return redirect(redirect_url)
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')