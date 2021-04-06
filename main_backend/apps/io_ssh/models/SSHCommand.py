from django.db import models

from taggit.managers import TaggableManager

from io_ssh.models.Device import Device


class SSHCommand(models.Model):
    command = models.CharField(max_length=500)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    tags = TaggableManager()

    @staticmethod
    def get_by_id(id_):
        try:
            return SSHCommand.objects.filter(device_id=id_)
        except SSHCommand.DoesNotExist:
            return []

    def connect_and_execute(self):
        pass
