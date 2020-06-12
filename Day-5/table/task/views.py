from django.shortcuts import render

# Create your views here.
def task(request):
	return render(request,'task/task.html')
def task2(request):
	return render(request,'task/task2.html')
def task3(request):
	return render(request,'task/task3.html')