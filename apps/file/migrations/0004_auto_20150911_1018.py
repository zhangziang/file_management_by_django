# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_file_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='add_time',
            field=models.DateField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
    ]
