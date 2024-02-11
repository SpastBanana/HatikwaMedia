from django.contrib import admin
from .models import song_list, song_files

class SongAdmin(admin.ModelAdmin):
    search_fields = ['song_name']

admin.site.register(song_list, SongAdmin)
admin.site.register(song_files)