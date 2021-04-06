from django.views import generic
from django.shortcuts import get_object_or_404

from io_ssh.models.SSHCommand import SSHCommand


class SSHCommandDetailView(generic.DetailView):
    model = SSHCommand
    template_name = "io_ssh/command_detail.html"

    def get_object(self):
        command = get_object_or_404(SSHCommand, id=self.kwargs["command_pk"])
        return command

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data
