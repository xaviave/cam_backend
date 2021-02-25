from django.db import models


class SshHandler(models.Model):
    """
    need a rsa key handler: - generate
                            - export
                            - import
    """

    username = models.CharField(max_length=50, null=False)
    host = models.CharField(max_length=50, null=False)
    port = models.CharField(max_length=4, null=False)
    password = models.CharField(max_length=50, null=False)
    ssh_key = models.TextField(null=False)
