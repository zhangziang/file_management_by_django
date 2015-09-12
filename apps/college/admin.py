# encoding: utf-8

from django.contrib import admin

from .models import College

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    pass
