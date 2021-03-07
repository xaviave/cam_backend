from django.views import generic

from io_ssh.models.Device import Device
from io_ssh.models.SSHCommand import SSHCommand


class IndexView(generic.ListView):
    template_name = "io_ssh/index.html"
    context_object_name = "latest_device_list"

    @staticmethod
    def get_queryset():
        return Device.objects.order_by("-create_date")[:5]


class DetailView(generic.DetailView):
    model = Device
    template_name = "io_ssh/detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        device_id = self.kwargs.get('pk')
        try:
            data['ssh_command_list'] = SSHCommand.objects.filter(device_id=device_id)
        except SSHCommand.DoesNotExist:
            data['ssh_command_list'] = []
        return data