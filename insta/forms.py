from django import forms


class PageForm(forms.Form):
	page = forms.CharField(label='IG Page', max_length=150)