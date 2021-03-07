from django.urls import path
from django.shortcuts import redirect

from io_ssh.views import views, create_from_request

app_name = "io_ssh"
urlpatterns = [
    path("", views.IndexView.as_view(), name="v"),
    path("v", lambda x: redirect(f"/")),
    path("device/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create_device/", create_from_request.create_device, name="create_device"),
    path(
        "device/<int:pk>/create_ssh_command/",
        create_from_request.create_ssh_command,
        name="create_ssh_command",
    ),
]
