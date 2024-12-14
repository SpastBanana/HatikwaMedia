from django.conf import settings
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from Backend.models import member_invites
from Songs.models import song_list


class SiteRestrictions:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')

        # Usable variables
        available_roles = ["Admin", "Bestuur", "Dirigent", "PR-lid"]
        user_authenticated = request.user.is_authenticated
        user_groups = request.user.groups.values_list('name',flat = True)
        authorised_urls = ["/login", "/gast", "/auth"]
        guest_activated = []

        for item in song_list.objects.all():
            if item.guest_active:
                guest_activated.append(item.song_name)
        

        # Rules if user is authenticated
        if user_authenticated:
            access = False

            if 'db' in request.path and 'Admin' not in user_groups:
                    raise PermissionDenied()

            if 'admin' in request.path and 'db' not in request.path:

                for role in available_roles:
                    if request.user.groups.filter(name=role).exists():
                        access = True
                
                # Determen access
                if access == False:
                    raise PermissionDenied()

        # Rules if user is not authenticated
        if not user_authenticated:
            access = False
            
            if "song" in request.path:
                song_path = request.path.split('/')[3]
                if song_path in guest_activated:
                    access = True
                else:    
                    return redirect('/')

            for item in authorised_urls:
                if item in request.path:
                    access = True

            # Determen access
            if access == False and request.path not in ['', '/']:
                raise PermissionDenied()

            if access == False and request.path in ['', '/']:
                return redirect('/login')