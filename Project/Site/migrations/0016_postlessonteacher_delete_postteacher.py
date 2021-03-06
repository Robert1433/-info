# Generated by Django 4.0.5 on 2022-07-03 11:18

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0015_rename_tiputilizator_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLessonTeacher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('teacher_user', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=1000)),
                ('update', models.FileField(upload_to='files')),
                ('imag', models.ImageField(upload_to='images')),
                ('creation_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='PostTeacher',
        ),
    ]
