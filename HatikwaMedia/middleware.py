from django.conf import settings
from django.http import Http500
from django.shortcuts import redirect

# class yo:

#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(slef, request):
#         response = self.get_response(request)
#         return response

#     def process_view(self, request, view_func, view_args, view_kwargs):
#         assert hasattr(request, 'user')

#         if not request.user.is_authenticated():
#             return redirect('/login')

#         if not request.user.groups.filter(name="Admin").exists():
#             raise Http500


class dbadmin:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response