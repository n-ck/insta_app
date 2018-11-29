# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .forms import PageForm


def index(request):
    return HttpResponse("Hello, world. You're at the insta index.")

class GetPage(ListView):

	def get(self, request):

		form = PageForm()

		# return HttpResponse("Yes, it works!")

		return render(request, 'page.html', {'form': form})

	def post(self, request):
		pass

		form = PageForm()

		if form.is_valid():
			# Process the data
			pass