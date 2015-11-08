# encoding: utf-8

from django.contrib import admin

from .models import Course
from ..file.models import File


class FileInline(admin.TabularInline):

    model = File
    # max_num = 1
    extra = 0
    readonly_fields = ['name', 'intro', 'the_file', 'add_time', 'edit_file_link']

    def has_add_permission(self, request):
        return False

    can_delete = False

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [
        FileInline,
    ]
