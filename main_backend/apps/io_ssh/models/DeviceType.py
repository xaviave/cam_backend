from django.db import models


class DeviceType(models.Model):
    model = models.CharField(max_length=255)
    version = models.CharField(max_length=20)
    model_link = models.URLField(max_length=255)
    gpio = models.BooleanField(default=True)

    class Meta:
        ordering = ["model"]
        verbose_name_plural = "Device Types"
        unique_together = ("model", "version", "gpio")

    def __str__(self):
        return f"{self.model} {self.version}"

    def device_type_printer(self):
        return (
            f"[{self.__str__()}] | {'There is ' if self.gpio else 'There is no '}GPIO"
        )
