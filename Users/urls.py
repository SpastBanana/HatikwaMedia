from django.contrib import admin
from django.urls import path, include
from . import users

urlpatterns = [
    path('', users.users, name="Create user"),
    path('create-user', users.create_user, name="Create user"),
    path('delete-user/<str:mail>', users.delete_user, name="Delete user"),
    path('delete-user/<str:mail>/delete', users.delete_user_confirmed, name="Delete user"),
    path('reset-user/<str:mail>', users.reset_user, name="Reset user"),
    path('reset-user/<str:mail>/reset', users.reset_user_confirmed, name="Reset user"),
]
