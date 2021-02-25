# Generated by Django 3.1.6 on 2021-02-07 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("io_ssh", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="device",
            unique_together={("name", "type")},
        ),
        migrations.AlterUniqueTogether(
            name="devicetype",
            unique_together={("model", "version", "gpio")},
        ),
    ]
