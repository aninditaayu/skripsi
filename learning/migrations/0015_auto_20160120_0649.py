# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0014_soal_isi_console'),
    ]

    operations = [
        migrations.AddField(
            model_name='jawaban',
            name='sudah_benar',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='materi',
            name='bab',
            field=models.ForeignKey(related_name=b'bab', to='learning.Bab'),
        ),
        migrations.AlterField(
            model_name='soal',
            name='materi',
            field=models.ForeignKey(related_name=b'materi', to='learning.Materi'),
        ),
    ]
