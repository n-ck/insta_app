# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .forms import PageForm

from bs4 import BeautifulSoup
import requests
import utils


def index(request):
    return HttpResponse("Hello, world. You're at the insta index.")

class GetPage(View):

	def get(self, request):

		form = PageForm()

		context = {
			'form': form,
			'answer': "",
		}

		return render(request, 'page.html', context)


	def post(self, request):
		
		form = PageForm(request.POST)
		response = None

		if form.is_valid():

			response = form.cleaned_data['page']

			r = requests.get(response)
			print r

			soup = BeautifulSoup(r.text, 'html.parser')

			print soup.title

			# print soup.script.text
			scriptlist = []
			for element in soup.find_all('script'):
				scriptlist.append(element.text)

			imgscript = scriptlist[4]

			imgurl = utils.get_post_img(imgscript) 

			context = {
				'form': form,
				'answer': imgurl
			}

			return render(request, 'page.html', context)
