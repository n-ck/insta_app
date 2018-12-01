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

		form = PageForm()

		context = {
			'form': form,
			'answer': "",
		}

		return render(request, 'post.html', context)

	def post(self, request):
		
		form = PageForm(request.POST)
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
