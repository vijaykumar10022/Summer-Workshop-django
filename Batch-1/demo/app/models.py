from django.db import models

# Create your models here.
class Emp(models.Model):
	name=models.CharField(max_length=20)
	salary=models.FloatField()
	age=models.IntegerField()
	desig=models.CharField(max_length=30)
