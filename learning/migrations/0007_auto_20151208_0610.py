# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0006_bab_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bab',
            name='slug',
        ),
        migrations.AddField(
            model_name='materi',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
