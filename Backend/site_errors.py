from django.shortcuts import render

def not_found(request, exception=None, template_name="errors/404.html"):
    return render(request, template_name, status=404)


def forbidden(request, exception=None, template_name="errors/403.html"):
    return render(request, template_name, status=403)


def lid_access_denied(request):
    return render(request, 'errors/lid-access-denied.html')


def not_registrated(request):
    return render(request, 'errors/not-registrated.html')