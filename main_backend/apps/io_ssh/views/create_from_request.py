from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from io_ssh.models.Device import Device
from io_ssh.models.SSHCommand import SSHCommand

from io_ssh.forms.DeviceForm import DeviceForm
from io_ssh.forms.SSHCommandForm import SSHCommandForm


def create_device(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Device.objects.update_or_create(
                name=form.cleaned_data["name"], type_id=form.cleaned_data["type"].pk
            )
            return HttpResponseRedirect(reverse("io_ssh:v"))
    else:
        form = DeviceForm()
    return render(request, "io_ssh/create_device.html", {"form": form})


def create_ssh_command(request, pk):
    if request.method == "POST":
        form = SSHCommandForm(request.POST)
        if form.is_valid():
            SSHCommand.objects.update_or_create(
                command=form.cleaned_data["command"], device_id=pk
            )
            return HttpResponseRedirect(
                reverse(f"io_ssh:device_detail", kwargs={"pk": pk})
            )
    else:
        form = SSHCommandForm()
    return render(
        request,
        f"io_ssh/create_ssh_command.html",
        {"form": form},
    )
