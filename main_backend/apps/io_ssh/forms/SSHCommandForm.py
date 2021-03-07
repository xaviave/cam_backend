from django import forms

from io_ssh.models.SSHCommand import SSHCommand


class SSHCommandForm(forms.ModelForm):
    command = forms.CharField(label="SSH command")

    class Meta:
        model = SSHCommand
        fields = [
            "command",
        ]
