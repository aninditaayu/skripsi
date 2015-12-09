# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0005_auto_20151208_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='bab',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
