# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='intro',
            field=models.TextField(default=b'', verbose_name='\u4ecb\u7ecd', blank=True),
        ),
    ]
