# Generated by Django 4.0.5 on 2022-07-03 10:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Site', '0014_tiputilizator_id_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TipUtilizator',
            new_name='Profile',
        ),
    ]
