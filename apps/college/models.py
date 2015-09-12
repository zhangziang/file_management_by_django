# encoding: utf-8

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class College(models.Model):
    name = models.CharField(max_length=400, verbose_name=u'学院名称')
    intro = models.TextField(verbose_name=u'学院介绍', blank=True, default='')

    class Meta:
        verbose_name = u'学院'
        verbose_name_plural = u'学院'

    def __str__(self):
        return self.name
