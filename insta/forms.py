from django import forms

TAGS = [
('cars', 'Cars'),
('inspiration', 'Inspiration'),
('other', 'Other'),
]

class PostForm(forms.Form):
	post = forms.CharField(label='IG Post URL', max_length=250)
	# tag = forms.CharField(label='Tag:', 
	# 					  widget=forms.Select(choices=TAGS))

class PageForm(forms.Form):
	page = forms.CharField(label='IG Page Name', max_length=150)


class TagForm(forms.Form):
	tag = forms.CharField(label='Tag:', 
						  widget=forms.Select(choices=TAGS), 
						  required=False
						  )
	new_tag = forms.CharField(label='Tag name:', max_length=250)