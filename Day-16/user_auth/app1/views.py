from django.shortcuts import render,redirect
from app1.forms import Myform
from django.http import HttpResponse
# Create your views here.
def register(request):
	if request.method=="POST":
		data=Myform(request.POST)
		if data.is_valid():
			data.save()
			return redirect('/login')
	form=Myform()
	return render(request,'app1/register.html',{'form':form})
def home(request):
	return render(request,'app1/home.html')