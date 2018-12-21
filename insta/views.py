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
		savedposts = SavePagePost.objects.all().order_by('-id')[:5]
		context = {
			'form': form,
			'page': "None",
			'post': "None",
			'recent': savedposts
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
				'page': pagename,
				'post': imgurl,
				'recent': ""
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
			allpages = IgPage.objects.all().order_by('-id')[:5]
			context = {
				'form': form,
				'page': "None",
				'pageurl': "",
				'posts': [],
				'allpages': allpages,
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


class PostDetail(View):

	def get(self, request, postid):

		post = SavePagePost.objects.get(pk=postid)
		next_post = post.id + 1
		previous_post = post.id - 1

		context = {
			'post': post,
			'next': next_post,
			'previous': previous_post
		}

		return render(request, 'post_detail.html', context)


	# Further development:
	# + after entering page, you see the first 10 posts, and you can tag and save to the database
	# + after entering ost url, you can save the post to database
	# + page with all saved post
	# - posts page should have all saved posts with filters by tag
	# - post detail page, you can see full size and change tag here
	# - manage tag page (create, delete or rename tags)
	# - rename variables with underscore in naming



