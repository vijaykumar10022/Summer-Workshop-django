from django.db import models

# Create your models here.
class Email(models.Model):
	email=models.EmailField(max_length=50,null=True,unique=True)
	password=models.CharField(max_length=20)
	