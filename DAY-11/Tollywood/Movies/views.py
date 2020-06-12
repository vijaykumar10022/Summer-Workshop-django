from django.shortcuts import render

from .forms import MovieForm

# Create your views here.


def addmovie(request):
	form=MovieForm()
	return render(request,'Movies/addmovie.html',{'form':form})