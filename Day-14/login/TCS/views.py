from django.shortcuts import render,redirect
from TCS.forms import Myform,Mylogin
from django.http import HttpResponse
from TCS.models import Emp
# Create your views here.
def register(request):
	if request.method == "POST":
		data=Myform(request.POST)
		if data.is_valid():
			data.save()
			return redirect('/login')
	form=Myform()
	return render(request,'TCS/register.html',{'form':form})
def login(request):
	if request.method=="POST":
		uname=request.POST['username']
		upsw=request.POST['password']
		data=Emp.objects.filter(username=uname,password=upsw)
		if data:
			return render(request,'TCS/home.html',{'data':uname})
		else:
			return HttpResponse("login Failed...!!!")
	form=Mylogin()
	return render(request,'TCS/login.html',{'form':form})