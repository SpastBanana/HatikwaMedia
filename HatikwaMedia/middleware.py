from django.conf import settings
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from Backend.models import member_invites


class DbAdmin:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')

        if "db" in request.path:
            if not request.user.is_authenticated:
                return redirect('/login')

            if not request.user.groups.filter(name="Admin").exists():
                raise PermissionDenied()


class SiteAdmin:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')

        if "admin" in request.path and "db" not in request.path:
            access = False
            
            if not request.user.is_authenticated:
                return redirect('/login')

            for role in ["Admin", "Bestuur", "Dirigent", "PR-lid"]:
                if request.user.groups.filter(name=role).exists():
                    access = True
            
            if access == False:
                raise PermissionDenied()