# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0008_auto_20151208_0613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materi',
            name='slug',
        ),
        migrations.AlterField(
            model_name='materi',
            name='bab',
            field=models.ForeignKey(to='learning.Bab'),
        ),
    ]
