from django.contrib import admin
from .models import user_permissions, music_permissions, media_permissions

admin.site.register(user_permissions)
admin.site.register(music_permissions)
admin.site.register(media_permissions)
