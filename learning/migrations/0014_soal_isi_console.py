# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0013_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='soal',
            name='isi_console',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
