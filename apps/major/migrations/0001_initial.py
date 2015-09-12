# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400, verbose_name='\u4e13\u4e1a\u540d\u79f0')),
                ('intro', models.TextField(verbose_name='\u4e13\u4e1a\u4ecb\u7ecd')),
                ('college', models.ForeignKey(verbose_name='\u5b66\u9662', to='college.College')),
            ],
            options={
                'verbose_name': '\u4e13\u4e1a',
                'verbose_name_plural': '\u4e13\u4e1a',
            },
        ),
    ]
