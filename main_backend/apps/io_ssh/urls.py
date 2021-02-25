from django.urls import path
from django.shortcuts import redirect

from io_ssh.views import views

app_name = "io_ssh"
urlpatterns = [
    path("", views.IndexView.as_view(), name="v"),
    path("v", lambda x: redirect(f"/")),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create_device/", views.create_device, name="create_device"),
]
