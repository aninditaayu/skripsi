# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0017_auto_20160211_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='jawaban',
            name='console_user',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
