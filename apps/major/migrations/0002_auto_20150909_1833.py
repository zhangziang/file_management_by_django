# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='intro',
            field=models.TextField(default=b'', verbose_name='\u4e13\u4e1a\u4ecb\u7ecd', blank=True),
        ),
    ]
