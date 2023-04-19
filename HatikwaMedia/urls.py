from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
import Frontend, Backend
from Backend import site_errors
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('db/admin', admin.site.urls),
    path('', include('Frontend.urls')),
    path('admin', include('Backend.urls')),
    path('lid-access-denied', Backend.site_errors.lid_access_denied, name="Lid access denied"),
    path('not-registrated', Backend.site_errors.not_registrated, name="Not logged in"),
    path('login', Backend.views.loginview, name="Login"),
    path('logout', Backend.views.logoutview, name="Logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = "Backend.site_errors.not_found"