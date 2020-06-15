from django.forms import ModelForm

from app1.models import Student

class myStudent(ModelForm):
	class Meta:
		model=Student
		fields='__all__' #['name','phno']