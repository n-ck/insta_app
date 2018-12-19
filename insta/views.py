# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
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

		form = PageForm(request.GET)
		
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
				'page': page,
				'pageurl': url,
				'posts': allimgs,
				'allpages': allpages
			}

			return render(request, 'page.html', context)

		else: 
			form = PageForm()
			context = {
				'form': form,
				'page': "",
				'pageurl': "",
				'posts': [],
				'allpages': [],
			}

			return render(request, 'page.html' , context)

	## Changed Page form to GET request:
	
	# def post(self, request):
		
	# 	form = PageForm(request.POST)

	# 	if form.is_valid():

	# 		page = form.cleaned_data['page']
	# 		url = utils.get_page_url(page)

	# 		request.session['page'] = page 

	# 		igpage = IgPage(page=page, url=url)
	# 		igpage.save()

	# 		allpages = IgPage.objects.all()

	# 		allimgs = utils.get_page_script(url)
	# 		# print allimgs

	# 		context = {
	# 			'form': form,
	# 			'page': page,
	# 			'pageurl': url,
	# 			'posts': allimgs,
	# 			'allpages': allpages
	# 		}

	# 		return render(request, 'page.html', context)


class SavePost(View):

	def get(self, request, **kwargs):

		igpage = kwargs.get('page')
		imgurl = kwargs.get('img')
		pageurl = "https://www.instagram.com/%s" % igpage

		# print "this is the img: %s and this the page: %s" % (imgurl, igpage)

		# Save to DB:
		saveigpost = SavePagePost(url=pageurl, page=igpage, img=imgurl)
		saveigpost.save()

		pagecontent = "Img saved! %s %s" % (igpage, imgurl)

		# return HttpResponse(pagecontent)

		redirecturl = '/page/?page=%s' % igpage
		return redirect(redirecturl)


class ViewSaved(View):

	def get(self, request):

		savedposts = SavePagePost.objects.all()

		context = {
			'posts': savedposts,
		}

		return render(request, 'saved_posts.html', context)


	# Further development:
	# - after entering page, you see the first 10 posts, and you can tag and save to the database
	# - posts page should have all saved posts with filters by tag
	# - page with all saved post, you can tag them there


