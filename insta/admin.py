# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import IgPage, SavePost, Tags

# Register your models here.

class IgPageAdmin(admin.ModelAdmin):
	list_display = ('page','url')

class SavePostAdmin(admin.ModelAdmin):
	list_display = ('page','url', 'img')

class TagAdmin(admin.ModelAdmin):
	list_display = ('tag','user')

admin.site.register(IgPage, IgPageAdmin)

admin.site.register(SavePost, SavePostAdmin)

admin.site.register(Tags, TagAdmin)