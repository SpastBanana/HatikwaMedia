from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.site_settings, name="Settings"),
    path('users', views.users, name="Create user"),
    path('users/create-user', views.create_user, name="Create user"),
    path('users/delete-user', views.delete_user, name="Create user"),
    path('users/manange-user', views.manage_user, name="Create user"),
]
