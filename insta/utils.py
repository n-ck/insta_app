import re

def get_post_img(rawscript):	

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