from django.shortcuts import render, redirect

# Create your views here.

def homeview(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    return render(request, 'index.html')