from django.shortcuts import render,redirect
from django.http import HttpResponse

from Movies.forms import MovieForm

from Movies.models import Movie

# Create your views here.


def home(request):
	return render(request,'Movies/home.html')

def addmovie(request):
	if request.method=="POST":
		form=MovieForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse('successfullyAdded')
	form=MovieForm()
	return render(request,'Movies/addmovie.html',{'form':form})

def showmovies(request):
	movies=Movie.objects.all()
	return render(request,'Movies/showmovies.html',{'movies':movies})
def delete(request,id):
	data=Movie.objects.get(id=id)
	data.delete()
	return redirect('/showmovies')
def update(request,actor_name):
	data=Movie.objects.get(actor_name=actor_name)
	if request.method=="POST":
		data=MovieForm(request.POST,request.FILES)
		if data.is_valid():
			data.save()
			return redirect('/showmovies')
	form=MovieForm(instance=data)
	return render(request,'Movies/update.html',{'form':form,'data':data})