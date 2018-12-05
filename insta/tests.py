# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpRequest
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from insta.views import GetPage

# Create your tests here.

class TestPageStatusCode(SimpleTestCase):
	# Tutorial source: https://wsvincent.com/django-testing-tutorial/
	# In terminal run: python manage.py test -v 1
	# or: python manage.py test -v 2

	def test_home_page_status_code(self):
		print "test home page status"
		response = self.client.get('/')
		self.assertEquals(response.status_code, 200)

	def test_page_status_code(self):
		print "test ig page status"
		response = self.client.get('/page/')
		self.assertEquals(response.status_code, 200)

	def test_post_status_code(self):
		print "test ig post page status"
		response = self.client.get('/post/')
		self.assertEquals(response.status_code, 200)


class TestGetPage(SimpleTestCase):

	def setUp(self):
		# code to get the request argument
		response = self.client.get('/page/')
		request = response.wsgi_request

	def test_page_post(self):
		pass
		# getpage = GetPage()
		# getpage.get(request)