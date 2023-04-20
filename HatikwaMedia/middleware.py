from django.conf import settings
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class dbadmin:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')

        if "/db" in request.path:
            if not request.user.is_authenticated:
                return redirect('/login')

            if not request.user.groups.filter(name="Admin").exists():
                raise PermissionDenied()