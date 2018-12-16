# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from models import IgPage, IgPost, SavePagePost

from .forms import PostForm, PageForm

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
			imgscript = utils.get_post_script(response, 4)
			imgurl = utils.get_post_src(imgscript) 

			pagescript = utils.get_post_script(response, 3)
			pagename= utils.get_page_from_post(pagescript)

			tag = form.cleaned_data['tag']

			igpost = IgPost(url=response, page=pagename, img=imgurl, tag=tag)
			igpost.save()

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
			'posts': [],
			'allpages': [],
		}

		return render(request, 'page.html' , context)


	def post(self, request):
		
		form = PageForm(request.POST)

		if form.is_valid():

			page = form.cleaned_data['page']
			url = utils.get_page_url(page)

			request.session['page'] = page 

			igpage = IgPage(page=page, url=url)
			igpage.save()

			allpages = IgPage.objects.all()

			allimgs = utils.get_page_script(url)
			# print allimgs

			context = {
				'form': form,
				'page': url,
				'posts': allimgs,
				'allpages': allpages
			}

			return render(request, 'page.html', context)


class SavePost(View):

	def get(self, request, **kwargs):

		igurl = kwargs.get('url')
		igpage = igurl.replace("https://www.instagram.com/", "")
		igimg = kwargs.get('img')
		print "this is the img: %s and this the page: %s" % (igimg, igpage)

		## Save to DB:
		# saveigpost = SavePagePost(url=igurl, page=igpage, img=igimg)
		# saveigpost.save()

		pagecontent = "Img saved! %s" % (igpage)

		return HttpResponse(pagecontent)


	# Further development:
	# - after entering page, you see the first 10 posts, and you can tag and save to the database
	# - posts page should have all saved posts with filters by tag
	# - page with all saved post, you can tag them there


