from django import forms
import utils

# TAGS = [
# ('cars', 'Cars'),
# ('inspiration', 'Inspiration'),
# ('other', 'Other'),
# ]

# TAGS = utils.tag_dropdown(1)

class PostForm(forms.Form):
	post = forms.CharField(label='IG Post URL', max_length=250)
	# tag = forms.CharField(label='Tag:', 
	# 					  widget=forms.Select(choices=TAGS))

class PageForm(forms.Form):
	page = forms.CharField(label='IG Page Name', max_length=150)


class TagForm(forms.Form):

	TAGS = utils.tag_dropdown(2)

	print TAGS

	tag = forms.CharField(label='Tag:', 
						  widget=forms.Select(choices=TAGS), 
						  required=False,
						  )

	new_tag = forms.CharField(label='Tag name:', max_length=250)

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user',None)
		super(TagForm, self).__init__(*args, **kwargs)
		self.fields['tag'] = forms.CharField(label='Tag:', 
							  widget=forms.Select(choices=utils.tag_dropdown(self.user)), 
							  required=False,
							  )

	# def tag_fields(self):

	# 	userid = self.user

	# 	TAGS = utils.tag_dropdown(userid)

	# 	print TAGS

	# 	tag = forms.CharField(label='Tag:', 
	# 						  widget=forms.Select(choices=TAGS), 
	# 						  required=False,
	# 						  )

	# 	new_tag = forms.CharField(label='Tag name:', max_length=250)


		

		
		# self.fields['user_id'].initial = self.user

		# self.TAGS = utils.tag_dropdown(self.user)
		