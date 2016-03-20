# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0018_jawaban_console_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.RemoveField(
            model_name='materi',
            name='views',
        ),
        migrations.AlterField(
            model_name='userprofilekey',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 3, 20)),
        ),
    ]
