# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400, verbose_name='\u6587\u4ef6\u540d')),
                ('intro', models.TextField(verbose_name='\u4ecb\u7ecd')),
                ('the_file', models.FileField(upload_to=b'files', verbose_name='\u6587\u4ef6')),
                ('course', models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='course.Course')),
            ],
            options={
                'verbose_name': '\u6587\u4ef6',
                'verbose_name_plural': '\u6587\u4ef6',
            },
        ),
    ]
