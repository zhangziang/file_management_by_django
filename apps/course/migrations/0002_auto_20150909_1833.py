# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='intro',
            field=models.TextField(default=b'', verbose_name='\u8bfe\u7a0b\u4ecb\u7ecd', blank=True),
        ),
    ]
