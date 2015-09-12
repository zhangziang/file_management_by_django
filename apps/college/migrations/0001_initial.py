# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400, verbose_name='\u5b66\u9662\u540d\u79f0')),
                ('intro', models.TextField(verbose_name='\u5b66\u9662\u4ecb\u7ecd')),
            ],
            options={
                'verbose_name': '\u5b66\u9662',
                'verbose_name_plural': '\u5b66\u9662',
            },
        ),
    ]
