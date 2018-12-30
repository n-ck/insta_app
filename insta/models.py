# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class IgPage(models.Model):
    page = models.CharField(max_length=250, null=True)
    url = models.CharField(max_length=2083, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class IgPost(models.Model):
	url = models.CharField(max_length=2083, null=True)
	page = models.CharField(max_length=250, null=True)
	img = models.CharField(max_length=2083, null=True)
	tag = models.CharField(max_length=250, null=True)
	# user = models.CharField(max_length=250, null=True)

class SavePagePost(models.Model):
	url = models.CharField(max_length=2083, null=True)
	page = models.CharField(max_length=250, null=True)
	img = models.CharField(max_length=2083, null=True)
	tag = models.CharField(max_length=250, null=True)
	# user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

class Tags(models.Model):
	# save all tags and link to user pk
	# tag = models.CharField(max_length=250, null=True)
	# user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	pass