# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='intro',
            field=models.TextField(default=b'', verbose_name='\u5b66\u9662\u4ecb\u7ecd', blank=True),
        ),
    ]
