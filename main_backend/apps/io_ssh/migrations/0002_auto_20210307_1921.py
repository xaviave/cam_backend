# Generated by Django 3.1.7 on 2021-03-07 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('io_ssh', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='ssh_commands',
        ),
        migrations.AddField(
            model_name='sshcommand',
            name='device',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='io_ssh.device'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='io_ssh.devicetype'),
        ),
    ]
