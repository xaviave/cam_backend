from django.db import models

from taggit.managers import TaggableManager

from io_ssh.models.Device import Device


class SSHCommand(models.Model):
    command = models.CharField(max_length=500)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    tags = TaggableManager()
