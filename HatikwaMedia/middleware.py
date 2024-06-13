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

        guest_activated = []
        for item in song_list.objects.all():
            if item.guest_active:
                guest_activated.append(item.song_name)

        if request.user.is_authenticated:
            if "db" in request.path:
                if not request.user.groups.filter(name="Admin").exists():
                    raise PermissionDenied()

            if "admin" in request.path and "db" not in request.path:
                access = False

                for role in ["Admin", "Bestuur", "Dirigent", "PR-lid"]:
                    if request.user.groups.filter(name=role).exists():
                        access = True
                
                if access == False:
                    raise PermissionDenied()

        if not request.user.is_authenticated:
            access = False
            authorised_urls = ["", "/", "/login", "/gast", "/auth"]
            
            if "song" in request.path:
                song_path = request.path.split('/')[3]
                if song_path in guest_activated:
                    access = True
                else:    
                    return redirect('/')

            for item in authorised_urls:
                if item in request.path:
                    access = True

            if access == False:
                raise PermissionDenied()