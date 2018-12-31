# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import IgPage, SavePost

# Register your models here.

class IgPageAdmin(admin.ModelAdmin):
	list_display = ('page','url')

class SavePostAdmin(admin.ModelAdmin):
	list_display = ('page','url', 'img')

admin.site.register(IgPage, IgPageAdmin)

admin.site.register(SavePost, SavePostAdmin)