# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0010_auto_20151208_0628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soal',
            old_name='soal',
            new_name='deskripsi_soal',
        ),
        migrations.AddField(
            model_name='soal',
            name='instruksi',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='soal',
            name='judul_soal',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
