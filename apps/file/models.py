# encoding: utf-8

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from ..course.models import Course


@python_2_unicode_compatible
class File(models.Model):
    name = models.CharField(max_length=400, verbose_name=u'文件名')
    intro = models.TextField(verbose_name=u'介绍', blank=True, default='')
    the_file = models.FileField(verbose_name=u'文件', upload_to='files')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    add_time = models.DateField(verbose_name=u'添加时间', auto_now_add=True)

    class Meta:
        verbose_name = u'文件'
        verbose_name_plural = u'文件'

    def __str__(self):
        return self.name
