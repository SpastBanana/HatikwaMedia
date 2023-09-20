from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .mail import auth_mail
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('/')
        else:
            data = {
                'error': 'Incorrect wachtwoord en/of gebruikersnaam',
            }
            return render(request, 'user/login.html', data)

    data = {
        'error': '',
    }

    return render(request, 'user/login.html', data)


def logoutview(request):
    logout(request)

    return redirect('/')


def site_settings(request):
    data = {
        'page': 'settings/home.html'
    }   

    return render(request, 'settings/index.html', data)


def users(request):
    data = {
        'page': 'settings/users.html',
    }

    return render(request, 'settings/index.html', data)


def create_user(request):
    data = {
        'page': 'settings/create-user.html',
        'notify': '',
        'users': User.objects.filter(groups__name='Lid'),
    }

    if request.method == 'POST' and 'create-user' in request.POST:
        form = member_invites()
        email = request.POST.get('email')

        auth_mail(email, 'Uitnodiging deelname Hatikwa-Media', email)

        try:
            user = User.objects.get(username=email)
            user.delete()
            user = User.objects.create_user(email, email, "HatikwaMediaManagement")
            user.save()

            try:
                member_invites.objects.get(email=email).delete()
                form.email = email
                form.save()
            except:
                form.email = email
                form.save()

        except User.DoesNotExist:
            user = User.objects.create_user(email, email, "HatikwaMediaManagement")
            user.save()

            form.email = email
            form.save()

        data = {
            'page': 'settings/create-user.html',
            'notify': 'Uitnodiging is verstuurd!',
            'users': User.objects.filter(groups__name='Lid'),
        }

    return render(request, 'settings/index.html', data)


def activate_user(request, mail):
    pending = []

    for person in member_invites.objects.all():
        pending.append(person.email)

    if mail in pending:
        data = {'error': ''}

        if request.method == "POST":
            pass1 = request.POST.get('pass')
            pass2 = request.POST.get('check')

            if pass1 == pass2:
                user = User.objects.get(username=mail)
                user.set_password(pass1)
                my_group = Group.objects.get(name='Lid')
                user.groups.add(my_group)
                user.save()

                member_invites.objects.get(email=mail).delete()
                
                return redirect('/login')

            elif pass1 != pass2:
                data = {'error': 'Wachtwoorden komen niet overeen'}
            
        return render(request, 'user/activate.html', data)
    else:
        raise PermissionDenied()


def delete_user(request):
    raise PermissionDenied()


def manage_user(request):
    raise PermissionDenied()