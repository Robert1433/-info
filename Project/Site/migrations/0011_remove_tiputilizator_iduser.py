# Generated by Django 4.0.5 on 2022-07-01 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0010_tiputilizator_iduser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tiputilizator',
            name='iduser',
        ),
    ]
