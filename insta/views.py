# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import IgPage, SavePost
from .forms import PostForm, PageForm, TagForm

import utils


def index(request):
    return render(request, 'index.html', {})


class GetPostImg(LoginRequiredMixin, View):

	def get(self, request):

		userid = request.user.pk

		form = PostForm()
		# savedposts = SavePagePost.objects.filter(user=userid).order_by('-id')[:5]
		# savedposts = SavePagePost.objects.all()
		context = {
			'form': form,
			'page': "None",
			'post': "None",
			'recent': "None",
			# 'recent': savedposts
		}

		return render(request, 'post.html', context)

	def post(self, request):

		userid = request.user.pk
		
		form = PostForm(request.POST)
		response = None

		if form.is_valid():

			response = form.cleaned_data['post']
			imgscript = utils.get_post_script(response, 4)
			imgurl = utils.get_post_src(imgscript) 

			pagescript = utils.get_post_script(response, 3)
			pagename= utils.get_page_from_post(pagescript)

			tag = form.cleaned_data['tag']

			# igpost = IgPost(url=response, page=pagename, img=imgurl, 
			# 				tag=tag, user=userid)
			# igpost.save()

			context = {
				'form': form,
				'page': pagename,
				'post': imgurl,
				'recent': ""
			}

			return render(request, 'post.html', context)


class GetPage(LoginRequiredMixin, View):

	def get(self, request):

		form = PageForm(request.GET)
		user = request.user
		
		if form.is_valid():
			
			page = form.cleaned_data['page']
			url = utils.get_page_url(page)

			request.session['page'] = page 

			igpage = IgPage(page=page, url=url, user=user)
			igpage.save()

			allpages = IgPage.objects.filter(user=user)

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
			allpages = IgPage.objects.filter(user=user).order_by('-id')[:5]
			context = {
				'form': form,
				'page': "None",
				'pageurl': "",
				'posts': [],
				'allpages': allpages,
			}

			return render(request, 'page.html' , context)


class SaveIgPost(View):

	def get(self, request, **kwargs):

		userid = request.user.pk
		igpage = kwargs.get('page')
		imgurl = kwargs.get('img')
		pageurl = "https://www.instagram.com/%s" % igpage

		# print "this is the img: %s and this the page: %s" % (imgurl, igpage)

		# Save to DB:
		saveigpost = SavePost(url=pageurl, page=igpage, img=imgurl, user=userid)
		saveigpost.save()

		pagecontent = "Img saved! %s %s" % (igpage, imgurl)

		# return HttpResponse(pagecontent)

		redirecturl = '/page/?page=%s' % igpage
		return redirect(redirecturl)


class ViewSaved(LoginRequiredMixin, View):

	def get(self, request):

		userid = request.user.pk
		savedposts = SavePost.objects.filter(user=userid)
		tags = savedposts.values('tag').distinct().exclude(tag=None)

		context = {
			'posts': savedposts,
			'tags': tags
		}

		return render(request, 'saved_posts.html', context)


class PostDetail(LoginRequiredMixin, View):

	def get(self, request, postid):

		userid = request.user.pk
		post = SavePost.objects.get(pk=postid)

		next_post = post.id + 1
		previous_post = post.id - 1

		form = TagForm()

		context = {
			'form': form, 
			'post': post,
			'next': next_post,
			'previous': previous_post,
			'tag': post.tag
		}

		if userid == post.user:
			return render(request, 'post_detail.html', context)
		else:
			return redirect('insta:view_saved')

	def post(self, request, postid):

		form = TagForm(request.POST)

		if form.is_valid():
			
			tag = form.cleaned_data['tag']

			post = SavePost.objects.get(pk=postid)
			next_post = post.id + 1
			previous_post = post.id - 1

			unique_tags = SavePost.objects.filter(tag=tag)

			post.tag = tag
			post.save()

			context = {
				'form': form,
				'post': post,
				'next': next_post,
				'previous': previous_post,
				'tag': post.tag
			}

			return render(request, 'post_detail.html', context)


class DeletePost(View):

	def get(self, request, postid):

		post = SavePost.objects.get(pk=postid)
		post.delete()

		return redirect('/savedposts/')


class ViewSavedTag(View):
	## page to see post with a certain tag only
	def get(self, request, tag):
		
		tagged_posts = SavePost.objects.filter(tag=tag)
		all_tags = SavePost.objects.all().values('tag').distinct().exclude(tag=None)


		context = {
			'posts': tagged_posts,
			'tags': all_tags,
		}

		return render(request, 'saved_posts.html', context)


class ManageTags(LoginRequiredMixin, View):

	def get(self, request):

		all_tags = SavePost.objects.all().values('tag').distinct().exclude(tag=None)

		context = {
			'tags': all_tags
		}

		return render(request, 'manage_tags.html', context)

	def post(self, request):
		pass


	# Further development:
	# + after entering page, you see the first 10 posts, and you can tag and save to the database
	# + after entering post url, you can save the post to database
	# + page with all saved post
	# + logic to delete post on detail page
	# - posts page should have all saved posts with filters by tag
	# - post detail page, you can see full size and change tag here
	# - manage tag page (create, delete or rename tags)
	# - rename variables with underscore in naming
	# - page view: sort by page
	# - page view: scroll view


	# Bug:
	# - Previous and next buttons on Saved Post detail page
	# - 



