from django.db import models

# Create your models here.
class MovieDetails(models.Model):
	moviename=models.CharField(max_length=50)
	hero=models.CharField(max_length=30)
	heroine=models.CharField(max_length=30)
	director=models.CharField(max_length=30)
	producer=models.CharField(max_length=30)
	budget=models.IntegerField(null=True)
	reldate=models.DateField(null=True)


