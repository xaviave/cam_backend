from django.contrib import admin

from io_ssh.models.Device import Device
from io_ssh.models.DeviceType import DeviceType


class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    list_filter = ("create_date",)


class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ("model", "version", "gpio")
    list_filter = ("model", "gpio")


admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceType, DeviceTypeAdmin)
