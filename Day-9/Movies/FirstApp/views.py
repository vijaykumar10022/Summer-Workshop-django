from django.shortcuts import render
from FirstApp.models import MovieDetails
from django.http import HttpResponse
# Create your views here.

def register(request):
	if request.method=='POST':
		rmovie=request.POST['movie']
		rhero=request.POST['hero']
		rheroine=request.POST['heroine']
		rdirector=request.POST['director']
		rproducer=request.POST['producer']
		rbudget=request.POST['budget']
		rreldate=request.POST['reldate']
		data=MovieDetails(moviename=rmovie,hero=rhero,
			heroine=rheroine,director=rdirector,producer=rproducer,
			budget=rbudget,reldate=rreldate)
		data.save()
		return HttpResponse('Data Registered Successfullly...!')
	return render(request,'FirstApp/register.html')

def Showdata(request):
	data=MovieDetails.objects.all()
	return render(request,'FirstApp/Showdata.html',{'data':data})
