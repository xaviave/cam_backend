from django import forms

from io_ssh.models.Device import Device
from io_ssh.models.DeviceType import DeviceType


class DeviceForm(forms.ModelForm):
    name = forms.CharField(label="Device name", max_length=255)
    type = forms.ModelChoiceField(
        label="Device model type",
        required=True,
        queryset=DeviceType.objects.all(),
    )

    class Meta:
        model = Device
        fields = "__all__"
