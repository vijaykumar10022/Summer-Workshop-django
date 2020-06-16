from django.db import models

# Create your models here.
class Emp(models.Model):
	name=models.CharField(max_length=30)
	age=models.IntegerField(null=True)
	mobile=models.IntegerField(null=True)
	email=models.EmailField(max_length=30)
	username=models.CharField(max_length=30)
	password=models.CharField(max_length=30)

