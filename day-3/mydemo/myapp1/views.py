from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
	return HttpResponse("<h1>Hello Every one Welcome Django Live session</h1>")

def hi(request):
	return HttpResponse("<h2>hi</h2>")