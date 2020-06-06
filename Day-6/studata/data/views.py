from django.shortcuts import render

# Create your views here.
def register(request):
	return render(request,'data/register.html')

def display(request):
	if request.method=="POST":
		name=request.POST['name']
		mailid=request.POST['mailid']
		pnno=request.POST['pnno']
		roll=request.POST['roll']
		address=request.POST['address']
		mydata={'name':name,'mailid':mailid,'pnno':pnno,'roll':roll,'address':address}
		
		return render(request,'data/display.html',{'data':mydata})
		# return render(request,'data/display.html',{'data':{'name':request.POST['name'],'mailid':request.POST['mailid'],'pnno':request.POST['pnno'],'roll':request.POST['roll'],'address':request.POST['address']}})