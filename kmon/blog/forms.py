from __future__ import unicode_literals
from django import forms
from .models import Photo
from .models import Comment
# from django.core.urlresolvers import reverse_lazy


class PhotoForm(forms.ModelForm):
	class Meta:
			model = Photo
			fields = ('Image_File', 'Content', )
			exclude = ('Filtered_Image_File',)
	Image_File = forms.ImageField()
	Filtered_Image_File = forms.ImageField()
	Content = forms.CharField(
		max_length = 500,
		required = False,
		widget = forms.Textarea
	)
	Created = forms.DateTimeField(required = False)

	def get_absolute_url(self):
		url = reverse_lazy('read', kwargs={'pk': self.pk})
		return url

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('Name', 'Content', 'Password')
