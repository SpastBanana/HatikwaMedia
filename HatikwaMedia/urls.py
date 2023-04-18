"""HatikwaMedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
import Frontend, Backend
from Backend import site_errors

urlpatterns = [
    path('db/admin', admin.site.urls),
    path('', include('Frontend.urls')),
    path('admin', include('Backend.urls')),
    path('lid-access-denied', Backend.site_errors.lid_access_denied, name="Lid access denied"),
    path('not-registrated', Backend.site_errors.not_registrated, name="Not logged in"),
    path('login', Backend.views.loginview, name="Login"),
    path('logout', Backend.views.logoutview, name="Logout"),
]

handler404 = "Backend.site_errors.not_found"