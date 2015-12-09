# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0009_auto_20151208_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='bab',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materi',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='materi',
            name='bab',
            field=models.ForeignKey(related_name=b'materi', to='learning.Bab'),
        ),
    ]
