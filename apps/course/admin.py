# encoding: utf-8

from django.contrib import admin

from .models import Course
from ..file.models import File


class FileInline(admin.TabularInline):
    model = File
    extra = 0
    readonly_fields = ['add_time', ]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [
        FileInline,
    ]
