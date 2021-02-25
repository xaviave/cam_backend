from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    # MY APPS
    path("polls/", include("polls.urls")),
    path("", lambda x: redirect(f"io_ssh/")),
    path("io_ssh/", include("io_ssh.urls")),
]
