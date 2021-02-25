from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect

from io_ssh.models.Device import Device

from io_ssh.forms.DeviceForm import DeviceForm


class IndexView(generic.ListView):
    template_name = "io_ssh/index.html"
    context_object_name = "latest_device_list"

    @staticmethod
    def get_queryset():
        return Device.objects.order_by("-create_date")[:5]


class DetailView(generic.DetailView):
    model = Device
    template_name = "io_ssh/detail.html"


def create_device(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            Device.objects.update_or_create(name=form.cleaned_data["name"], type_id=1)
            return HttpResponseRedirect(reverse("io_ssh:v"))
    else:
        form = DeviceForm()
    return render(request, "io_ssh/create_device.html", {"form": form})
