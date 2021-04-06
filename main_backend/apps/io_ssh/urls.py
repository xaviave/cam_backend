from django.urls import path
from django.shortcuts import redirect

from io_ssh.views.IndexView import IndexView
from io_ssh.views.DeviceDetailView import DeviceDetailView
from io_ssh.views.SSHCommandDetailView import SSHCommandDetailView
from io_ssh.views.execute_from_request import execute_command
from io_ssh.views.create_from_request import create_device, create_ssh_command

app_name = "io_ssh"

urlpatterns = [
    path("", IndexView.as_view(), name="v"),
    path("v", lambda x: redirect(f"/")),
    path("device/<int:device_pk>/", DeviceDetailView.as_view(), name="device_detail"),
    path("create_device/", create_device, name="create_device"),
    path(
        "device/<int:pk_device>/create_ssh_command/",
        create_ssh_command,
        name="create_ssh_command",
    ),
    path(
        "device/<int:pk_device>/command/<int:command_pk>/",
        SSHCommandDetailView.as_view(),
        name="command_detail",
    ),
    path(
        "device/<int:pk_device>/command/<int:command_pk>/execute_command/",
        execute_command,
        name="execute_command",
    ),
]
