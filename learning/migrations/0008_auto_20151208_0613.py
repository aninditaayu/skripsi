# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_auto_20151208_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materi',
            name='bab',
            field=models.ForeignKey(related_name=b'materi', to='learning.Bab'),
        ),
    ]
