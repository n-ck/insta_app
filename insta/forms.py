from django import forms


class PageForm(forms.Form):
	page = forms.CharField(label='IG Post URL', max_length=150)