from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def table(request,num):
	data=[]
	for i in range(1,11):
		td=str(num)+" * "+str(i)+" = "+str(num*i)
		data.append(td)
	# print(data)
		# print(str(num)+" * "+str(i)+" = "+str(num*i))	
	return render(request,'app1/table.html',{'info':data,'table':num,'len':len(data)+1})

def add(request):
	return render(request,'app1/add.html')