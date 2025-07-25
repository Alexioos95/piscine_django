from django.db import models

class Movies(models.Model):
	episode_nb = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=64, unique=True)
	opening_crawl = models.TextField(null=True, blank=True)
	director = models.CharField(max_length=32)
	producer = models.CharField(max_length=128)
	release_date = models.DateField()

	def	__str__(self):
		return self.title
