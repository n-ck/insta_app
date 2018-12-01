from bs4 import BeautifulSoup
import requests
import re


def get_post_script(posturl):

	r = requests.get(posturl)
	soup = BeautifulSoup(r.text, 'html.parser')

	# Get all javascript from the page:
	scriptlist = []
	for element in soup.find_all('script'):
		scriptlist.append(element.text)

	return scriptlist[4]


def get_post_src(rawscript):	
	## Used this regex generator: txt2re.com

	re1='.*?'	# Non-greedy match on filler
	re2='(display)'	# Word 1
	re3='.*?'	# Non-greedy match on filler
	re4='((?:http|https)(?::\\/{2}[\\w]+)(?:[\\/|\\.]?)(?:[^\\s"]*))'	# HTTP URL 1

	rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
	m = rg.search(rawscript)

	if m:
		word=m.group(1)
		httpurl=m.group(2)
		
	return httpurl


def get_page_url(pagename):
	## Get IG Page Name

	pageurl = "https://www.instagram.com/%s" % pagename
	return pageurl


def get_page_script(pageurl):

	r = requests.get(pageurl)
	soup = BeautifulSoup(r.text, 'html.parser')

	# Get all javascript from the page:
	scriptlist = []
	for element in soup.find_all('script'):
		scriptlist.append(element.text)

	return get_page_imgs(scriptlist[3])


def get_page_imgs(pagescript):

	re1='.*?'	# Non-greedy match on filler
	re2='(display)'	# Word 1
	re3='.*?'	# Non-greedy match on filler
	re4='((?:http|https)(?::\\/{2}[\\w]+)(?:[\\/|\\.]?)(?:[^\\s"]*))'	# HTTP URL 1

	rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
	m = rg.search(pagescript)

	result = re.findall(rg, pagescript)

	for images in result:
		print images
		