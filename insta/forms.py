from django import forms


class PostForm(forms.Form):
	post = forms.CharField(label='IG Post URL', max_length=250)

class PageForm(forms.Form):
	page = forms.CharField(label='IG Page Name', max_length=150)