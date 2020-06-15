from django.shortcuts import render,redirect
from app1.forms import myStudent
from django.http import HttpResponse
from app1.models import Student
# Create your views here.
def add_data(request):
	if request.method =="POST":
		data=myStudent(request.POST)
		data.save()
		# return HttpResponse("Data Added Sucessfully...!!!")
		return redirect('/display')

	mydata=myStudent()
	return render(request,'app1/add_data.html',{'form':mydata})
def display(request):
	data=Student.objects.all()
	return render(request,'app1/display.html',{'mydata':data})
def trash(request,id):
	data=Student.objects.get(id=id)
	data.delete()
	# return HttpResponse("Data Deleted Sucessfully...!!!")
	return redirect('/display')
def update(request,id):
	data=Student.objects.get(id=id)
	if request.method =="POST":
		data=myStudent(request.POST)
		data.save()
		return redirect('/display')
	form=myStudent(instance=data)
	return render(request,'app1/update.html',{'form':form,'data':data})