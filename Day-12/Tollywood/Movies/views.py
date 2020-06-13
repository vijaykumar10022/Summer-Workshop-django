from django.shortcuts import render
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