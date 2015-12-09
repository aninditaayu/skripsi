# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning', '0004_auto_20151208_0448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jawaban',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jawaban', models.TextField()),
                ('waktu_jawab', models.DateTimeField(auto_now_add=True)),
                ('kali_jawab', models.IntegerField(default=0)),
                ('soal', models.ForeignKey(to='learning.Soal')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='soal',
            old_name='jawaban',
            new_name='kunci_jawaban',
        ),
    ]
