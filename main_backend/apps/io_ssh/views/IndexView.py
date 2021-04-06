from django.views import generic

from io_ssh.models.Device import Device


class IndexView(generic.ListView):
    template_name = "io_ssh/index.html"
    context_object_name = "latest_device_list"

    @staticmethod
    def get_queryset():
        return Device.objects.order_by("-create_date")[:5]
