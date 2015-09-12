# encoding: utf-8

from django.contrib import admin

from .models import File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    readonly_fields = ['add_time', ]
