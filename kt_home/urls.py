"""
URL configuration for kt_home project.
"""
from django.contrib import admin
from django.urls import path, include

from kt_home.views import index, robots

urlpatterns = [
    path("", index),
    path("/robots.txt", robots),

    path("auth/", include("auths.urls")),
    path("admin/", admin.site.urls),
]
