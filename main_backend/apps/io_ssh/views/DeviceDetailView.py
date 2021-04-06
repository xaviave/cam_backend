from django.views import generic
from django.shortcuts import get_object_or_404

from io_ssh.models.Device import Device
from io_ssh.models.SSHCommand import SSHCommand


class DeviceDetailView(generic.DetailView):
    model = Device
    template_name = "io_ssh/device_detail.html"

    def get_object(self):
        return get_object_or_404(Device, id=self.kwargs["device_pk"])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["ssh_command_list"] = SSHCommand.get_by_id(self.kwargs["device_pk"])
        return data
