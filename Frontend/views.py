from django.shortcuts import render, redirect

# Create your views here.

def homeview(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    data = {
        'page': 'home.html'
    }

    return render(request, 'index.html', data)