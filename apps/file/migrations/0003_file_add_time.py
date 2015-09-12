# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20150909_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 2, 3, 7, 351790, tzinfo=utc), verbose_name='\u6dfb\u52a0\u65f6\u95f4', auto_created=True),
            preserve_default=False,
        ),
    ]
