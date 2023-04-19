from django.contrib import admin
from .models import song_list, song_sheetfiles, song_soundfiles, song_mediafiles, song_otherfiles

admin.site.register(song_list)
admin.site.register(song_sheetfiles)
admin.site.register(song_soundfiles)
admin.site.register(song_mediafiles)
admin.site.register(song_otherfiles)