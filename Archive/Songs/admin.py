from django.contrib import admin
from .models import song_list, song_files

admin.site.register(song_list)
admin.site.register(song_files)