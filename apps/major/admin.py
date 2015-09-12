# encoding: utf-8

from django.contrib import admin

from .models import Major

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    pass
