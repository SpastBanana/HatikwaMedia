from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.site_settings, name="Settings"),
    path('create-user', views.create_user, name="Create user"),
]
