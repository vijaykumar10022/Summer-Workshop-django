from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.forms import Myform
from app.models import Emp
# Create your views here.
def hello(req):
	return HttpResponse("<h1>Hello</h1>")
def register(req):
	if req.method=="POST":
		data=Myform(req.POST)
		data.save()
		return redirect('/display')
	form=Myform()
	return render(req,'app/register.html',{'form':form})
def display(req):
	data=Emp.objects.all()
	return render(req,'app/display.html',{'mydata':data})