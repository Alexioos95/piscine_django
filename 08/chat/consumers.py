from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import User, ChatRoom, Message
import json

connected_users = {}

class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		# Set variables
		self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
		self.room_group_name = f"chat_{self.room_name}"
		self.username = self.scope["user"].username
		room_instance = await self.get_room(self.room_name)
		last_msgs = await self.get_last_messages(room_instance)
		# Add new user to group
		await self.channel_layer.group_add(self.room_group_name, self.channel_name)
		await self.accept()
		connected_users.setdefault(self.room_name, set()).add(self.username)
		# Send last 3 messages from room
		for l_msg in last_msgs:
			await self.send(text_data=json.dumps({
				"type": "chat_message",
				"msg": l_msg["msg"],
				"user": l_msg["user"],
			}))
		# Send to everyone the connection log
		await self.channel_layer.group_send(
			self.room_group_name,
			{
				"type": "chat_message",
				"msg": f"{self.username} has joined the chat",
				"user": "System"
			}
		)
		# Send to everyone new user_list
		await self.channel_layer.group_send(
			self.room_group_name,
			{
				"type": "user_list",
				"users": list(connected_users[self.room_name]),
			}
		)

	async def disconnect(self, close_code):
		# Remove user from group
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name
		)
		if self.room_name in connected_users:
			connected_users[self.room_name].discard(self.username)
		# Send to everyone new user_list
		await self.channel_layer.group_send(
			self.room_group_name,
			{
				"type": "user_list",
				"users": list(connected_users.get(self.room_name, [])),
			}
		)
		# Send to everyone the disconnection log
		await self.channel_layer.group_send(
			self.room_group_name,
			{
				"type": "chat_message",
				"msg": f"{self.username} has left the chat",
				"user": "System",
			}
		)

	async def receive(self, text_data):
		# Set variables
		data = json.loads(text_data)
		msg = data["msg"]
		room_instance = await self.get_room(self.room_name)
		user_instance = await self.get_user(self.username)
		# Add message to database
		await self.add_to_db(user_instance, msg, room_instance)
		# Send to everyone the message
		await self.channel_layer.group_send(
			self.room_group_name,
			{
				"type": "chat_message",
				"msg": msg,
				"user": self.username,
			}
		)

	# Message handlers
	async def chat_message(self, event):
		await self.send(text_data=json.dumps({
			"type": "chat_message",
			"msg": event["msg"],
			"user": event["user"],
		}))

	async def user_list(self, event):
		await self.send(text_data=json.dumps({
			"type": "user_list",
			"users": event["users"]
		}))

	# ORM helpers
	@database_sync_to_async
	def get_room(self, room_name):
		return ChatRoom.objects.get(name=room_name)

	@database_sync_to_async
	def get_last_messages(self, room_instance):
		last_msgs = Message.objects.filter(room=room_instance).order_by("-date")[:3]
		last_msgs = list(reversed(last_msgs))
		return [
			{
				"msg": msg.text,
				"user": msg.user.username,
				"date": msg.date.isoformat(),
			}
			for msg in last_msgs
		]

	@database_sync_to_async
	def get_user(self, user):
		return User.objects.get(username=user)

	@database_sync_to_async
	def add_to_db(self, user, msg, room_instance):
		msg = Message(room=room_instance, user=user, text=msg)
		msg.save()
