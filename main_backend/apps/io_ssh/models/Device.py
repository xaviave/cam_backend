from django.db import models

from io_ssh.models.DeviceType import DeviceType


class Device(models.Model):
    create_date = models.DateTimeField("date created", auto_now_add=True, blank=False)
    name = models.CharField(max_length=50)
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Devices"
        unique_together = ("name", "type")
