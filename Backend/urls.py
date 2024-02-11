from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler403
from django.conf import settings
from django.conf.urls.static import static

from . import views
import Users

urlpatterns = [
    path('', views.site_settings, name="Settings"),
    path('users/', include('Users.urls')),
    # path('users', users.users, name="Create user"),
    # path('users/create-user', users.create_user, name="Create user"),
    # path('users/delete-user', users.delete_user, name="Create user"),
    # path('users/manage-user', users.manage_user, name="Manage user"),
]
