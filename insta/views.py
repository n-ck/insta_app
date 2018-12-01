# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .forms import PageForm

import utils


def index(request):
    return HttpResponse("Hello, world. You're at the insta index.")

class GetPostImg(View):

	def get(self, request):

		form = PostForm()
		context = {
			'form': form,
			'answer': "",
		}

		return render(request, 'post.html', context)

	def post(self, request):
		
		form = PostForm(request.POST)
		response = None

		if form.is_valid():

			response = form.cleaned_data['post']
			imgscript = utils.get_post_script(response)
			imgurl = utils.get_post_src(imgscript) 

			context = {
				'form': form,
				'answer': imgurl
			}

			return render(request, 'post.html', context)


class GetPage(View):

	def get(self, request):
		
		form = PageForm()
		context = {
			'form': form,
			'page': "",
			'img': {}
		}

		return render(request, 'page.html' , context)


	def post(self, request):
		
		form = PageForm(request.POST)

		if form.is_valid():

			response = form.cleaned_data['page']
			page = utils.get_page_url(response)
			print utils.get_page_script(page)

			context = {
				'form': form,
				'page': page,
				'img': {},
			}

			return render(request, 'page.html', context)


