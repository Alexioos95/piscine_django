from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

class Message(models.Model):
	room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="chat_room")
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField(null=False, blank=False)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["date"]
