# encoding: utf-8

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ..major.models import Major


@python_2_unicode_compatible
class Course(models.Model):
    name = models.CharField(max_length=400, verbose_name=u'课程名称')
    intro = models.TextField(verbose_name=u'课程介绍', blank=True, default='')
    teacher = models.CharField(max_length=400, verbose_name=u'授课老师')
    major = models.ForeignKey(Major, verbose_name=u'专业')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = u'课程'

    def __str__(self):
        return self.name
