# Generated by Django 3.1.7 on 2021-03-07 16:58

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
    ]

    operations = [
        migrations.CreateModel(
            name="SSHCommand",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("command", models.CharField(max_length=500)),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeviceType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model", models.CharField(max_length=255)),
                ("version", models.CharField(max_length=20)),
                ("model_link", models.URLField(max_length=255)),
                ("gpio", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name_plural": "Device Types",
                "ordering": ["model"],
                "unique_together": {("model", "version", "gpio")},
            },
        ),
        migrations.CreateModel(
            name="Device",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date created"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "ssh_commands",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="io_ssh.sshcommand",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="io_ssh.devicetype",
                        verbose_name="model",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Devices",
                "ordering": ["name"],
                "unique_together": {("name", "type")},
            },
        ),
    ]
