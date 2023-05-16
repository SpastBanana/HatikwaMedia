from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name="Songs"),
    path('songs', views.homeview, name="Songs"),
    path('songs/song/<str:url_song_name>', views.songview, name="Songs"),
]