from django.shortcuts import render, redirect
from Songs.models import song_list

# Create your views here.

def homeview(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    data = {
        'page': 'home.html',
        'songs': song_list.objects.all()
    }

    return render(request, 'index.html', data)