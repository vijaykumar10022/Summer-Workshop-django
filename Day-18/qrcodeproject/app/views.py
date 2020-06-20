from django.shortcuts import render
import random
import qrcode
# Create your views here.
ootp=0
def login(request):
	if request.method=="POST":
		username=request.POST['uname']
		password=request.POST['psw']
		if username=="vijay" and password=="apssdc":
			otp=random.randint(10000,99999)
			global ootp
			ootp=otp
			print(otp,ootp,username)
			image=qrcode.make("Hello "+username+"your OTP is :"+str(otp))
			image.save(r"app/static/qrcodeimage/otp.jpg")
			return render(request,'app/qrcode.html',{'username':username})
	return render(request,'app/login.html')

def qrvalidation(request):
	otp=request.POST['otp']
	if otp==str(ootp):
		return render(request,'app/home.html')