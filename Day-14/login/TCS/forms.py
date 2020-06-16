from django.forms import ModelForm
from TCS.models import Emp
# for cretion for register page
class Myform(ModelForm):
	class Meta:
		model=Emp
		fields='__all__'
# for creation of login page
class Mylogin(ModelForm):
	class Meta:
		model=Emp
		fields=['username','password',]