from django.shortcuts import render
from django.core.mail import send_mail
import random
from FirstApp.models import Email
from django.http import HttpResponse
from EmailSend import settings
# Create your views here.

def index(request):
	if request.method=='POST':
		uemail=request.POST['email']
		pword=str(random.randint(100000,999999))
		data=Email(email=uemail,password=pword)
		data.save()
		sub='Reg to Your Login Deatils'
		body='''Hello {},\n\n\n Your UserName is :{}\n\n Your Password is:{}\n\n'''.format(uemail,uemail,pword)
		receiver=uemail
		sender=settings.EMAIL_HOST_USER
		send_mail(sub,body,sender,[receiver])
		return HttpResponse('Please check your Email Id')

	return render(request,'index.html')

def login(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		data=Email.objects.filter(email=email,password=password)
		if data:
			return HttpResponse('Welcome to User')
		else:
			return HttpResponse('Invalid User')
	return render(request,'login.html')
