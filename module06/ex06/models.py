from datetime import datetime
from django.db import models


class Tip(models.Model):
	content = models.TextField()
	author = models.ForeignKey("ex04.MyUser", on_delete=models.CASCADE, related_name="ex06_tips")
	date = models.DateTimeField(default=datetime.now)

	class Meta:
		permissions = [
			("downvote_tip", "Can downvote any tip"),
		]

	def up_count(self):
		return self.votes.filter(type="up").count()

	def down_count(self):
		return self.votes.filter(type="down").count()

	def __str__(self):
		return f"{self.author}: {self.content} - {self.date}"

class Vote(models.Model):
	type = models.CharField(max_length=4)
	user = models.ForeignKey("ex04.MyUser", on_delete=models.CASCADE, related_name="ex06_votes")
	tip = models.ForeignKey(Tip, on_delete=models.CASCADE, related_name="votes")

	class Meta:
		unique_together = ("user", "tip")
