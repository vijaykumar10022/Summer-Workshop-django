from django.forms import ModelForm # from django import forms

from Movies.models import Movie



class MovieForm(ModelForm):
	class Meta:

		model=Movie

		fields='__all__' #['tittle_name','poster']