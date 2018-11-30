# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .forms import PageForm

from bs4 import BeautifulSoup

def index(request):
    return HttpResponse("Hello, world. You're at the insta index.")

class GetPage(View):

	def get(self, request):

		form = PageForm()

		context = {
			'form': form,
			'answer': None,
		}

		# return HttpResponse("Yes, it works!")

		return render(request, 'page.html', context)

	def post(self, request):
		
		form = PageForm(request.POST)

		response = form['page']

		context = {
			'form': form,
			'answer': response
		}

		if form.is_valid():
			return render(request, 'page.html', context)