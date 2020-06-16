from django.forms import ModelForm

from app.models import Emp

class Myform(ModelForm):
	class Meta:
		model=Emp
		fields='__all__'