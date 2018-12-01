# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .forms import PageForm

from bs4 import BeautifulSoup
import re
import requests

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

			re1='.*?'	# Non-greedy match on filler
			re2='(display)'	# Word 1
			re3='.*?'	# Non-greedy match on filler
			re4='((?:http|https)(?::\\/{2}[\\w]+)(?:[\\/|\\.]?)(?:[^\\s"]*))'	# HTTP URL 1

			rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
			m = rg.search(imgscript)

			if m:
			    word1=m.group(1)
			    httpurl1=m.group(2)
			    print httpurl1

			# for img in soup.find_all('img'):
			# 	print (img.get('src'))

			context = {
				'form': form,
				'answer': soup.title
			}



			return render(request, 'page.html', context)