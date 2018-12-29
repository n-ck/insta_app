# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import IgPage, IgPost, SavePagePost

# Register your models here.

class IgPageAdmin(admin.ModelAdmin):
	list_display = ('page','url')

class IgPostAdmin(admin.ModelAdmin):
	list_display = ('page','url', 'img')


class SavePagePostAdmin(admin.ModelAdmin):
	list_display = ('page','url', 'img')

admin.site.register(IgPage, IgPageAdmin)

admin.site.register(IgPost, IgPostAdmin)

admin.site.register(SavePagePost, SavePagePostAdmin)