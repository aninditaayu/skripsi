# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0016_userprofilekey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilekey',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 2, 11)),
        ),
    ]
