from django.urls import path
from . import views

urlpatterns = [
	path("", views.chatroom_list, name="chatroom_list"),
	path("<str:chatroom_name>/", views.chat_room, name="chat_room"),
]
