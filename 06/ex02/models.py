from django.db import models
from datetime import datetime

class MyUser(models.Model):
	username = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.username

class Tip(models.Model):
	content = models.TextField()
	author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	date = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return f"{self.author}: {self.content} - {self.date}"
