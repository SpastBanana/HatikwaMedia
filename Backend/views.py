from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import member_invites
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group


def loginview(request):
    if request.user.is_authenticated:
        return redirect("/")
        
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('/')
        else:
            data = {
                'error': 'Incorrect wachtwoord en/of gebruikersnaam',
            }
            return render(request, 'login.html', data)

    data = {
        'error': '',
    }

    return render(request, 'login.html', data)


def logoutview(request):
    logout(request)

    return redirect('/')


def site_settings(request):
    data = {
        'page': 'settings/home.html'
    }   

    return render(request, 'settings/index.html', data)