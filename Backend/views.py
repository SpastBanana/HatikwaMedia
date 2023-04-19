from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

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

    user = request.user

    if not user.is_authenticated:
        return redirect('/not-registrated')
    if request.user.groups.filter(name="Lid").exists():
        if not user.groups.count() > 1:
            return redirect('/lid-access-denied')
    

    return render(request, 'settings/index.html', data)