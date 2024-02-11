from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler403
import Frontend, Backend, Users
from Backend import site_errors
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('db/admin/', admin.site.urls),
    path('', include('Frontend.urls')),
    path('admin/', include('Backend.urls')),
    path('login', Backend.views.loginview, name="Login"),
    path('logout', Backend.views.logoutview, name="Logout"),
    path('auth/new-member/register/<str:mail>', Users.users.activate_user, name="Activate user"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = "Backend.site_errors.not_found"
handler403 = "Backend.site_errors.forbidden"