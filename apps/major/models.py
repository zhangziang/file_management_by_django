# encoding: utf-8

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ..college.models import College


@python_2_unicode_compatible
class Major(models.Model):
    name = models.CharField(max_length=400, verbose_name=u'专业名称')
    intro = models.TextField(verbose_name=u'专业介绍', blank=True, default='')
    college = models.ForeignKey(College, verbose_name=u'学院')

    class Meta:
        verbose_name = u'专业'
        verbose_name_plural = u'专业'

    def __str__(self):
        return self.name
