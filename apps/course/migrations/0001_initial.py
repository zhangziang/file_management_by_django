# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400, verbose_name='\u8bfe\u7a0b\u540d\u79f0')),
                ('intro', models.TextField(verbose_name='\u8bfe\u7a0b\u4ecb\u7ecd')),
                ('teacher', models.CharField(max_length=400, verbose_name='\u6388\u8bfe\u8001\u5e08')),
                ('major', models.ForeignKey(verbose_name='\u4e13\u4e1a', to='major.Major')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
    ]
