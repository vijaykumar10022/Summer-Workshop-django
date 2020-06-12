from django.db import models

# Create your models here.

class Student(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	username=models.CharField(max_length=20)
	age=models.IntegerField(null=True)

	def __str__(self):
		return self.first_name +'-->'+self.last_name +"-->"+self.username+'-->'+str(self.age)

class Faculty(models.Model):
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=30,null=True)
	degi=models.CharField(max_length=30)
	age=models.IntegerField(null=True)
	email=models.EmailField(null=True)

	def __str__(self):
		return self.username +" "+self.degi+" "+str(self.age)+" "+self.email


	