from django.db import models

# Create your models here.
class Movie(models.Model):
	actors=[('Balakrishna','balakrishna'),
			('Nargarjuna','nargarjuna'),
			('Maheshbabu','maheshbabu'),
			('JrNtr','jrNtr'),
			('Phrabas','phrabas')]
	actress=[('Samantha','Samantha'),
			('Shriya Saran','Shriya Saran'),
			('Anushka Shetty','Anushka Shetty'),
			('Tamannaah','Tamannaah'),
			('Nayanthara','Nayanthara'),
			("Ileana D'Cruz","Ileana D'Cruz")]
	directors=[('S. S. Rajamouli','S. S. Rajamouli'),
				('Trivikram Srinivas','Trivikram Srinivas'),
				('Puri Jagannadh','Puri Jagannadh')]
	producers=[('Suresh Babu','Suresh Babu'),
				('Dasari Narayana Rao','Dasari Narayana Rao'),
				('Raghavendra Rao','Raghavendra Rao')]
	vardict=[('All Time Blockbuster','All Time Blockbuster'),
				('Blockbuster','Blockbuster'),
				('superhit','superhit'),('Average','Average')]
	title_name=models.CharField(max_length=50)
	poster=models.ImageField(upload_to="posters/")
	movie_images=models.ImageField(upload_to="albums/")
	actor_name=models.CharField(max_length=30,choices=actors)
	actress_name=models.CharField(max_length=30,choices=actress)
	director=models.CharField(max_length=30,choices=directors)
	producer=models.CharField(max_length=30,choices=producers)
	story_line=models.TextField(max_length=2000)
	trailer=models.FileField(upload_to='posters/')
	releasedate=models.DateTimeField(null=True)
	vardict=models.CharField(max_length=30,choices=vardict)

	def __str__(self):
		return self.title_name+' '+self.actor_name+' '+self.actress_name