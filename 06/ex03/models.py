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

	def up_count(self):
		return self.votes.filter(type="up").count()

	def down_count(self):
		return self.votes.filter(type="down").count()

	def __str__(self):
		return f"{self.author}: {self.content} - {self.date}"

class Vote(models.Model):
	type = models.CharField(max_length=4)
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	tip = models.ForeignKey(Tip, on_delete=models.CASCADE, related_name="votes")

	class Meta:
		unique_together = ('user', 'tip')
