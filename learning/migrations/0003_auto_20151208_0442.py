# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_auto_20151208_0418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(unique=True, max_length=128)),
                ('deskripsi', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('judul_materi', models.CharField(max_length=128)),
                ('deskripsi', models.TextField(null=True)),
                ('views', models.IntegerField(default=0)),
                ('bab', models.ForeignKey(to='learning.Bab')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Soal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('soal', models.TextField()),
                ('jawaban', models.TextField()),
                ('hint', models.TextField()),
                ('materi', models.ForeignKey(to='learning.Materi')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='page',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
