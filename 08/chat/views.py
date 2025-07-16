from django.shortcuts import render, get_object_or_404
from .models import ChatRoom
from django.contrib.auth.decorators import login_required

def chatroom_list(request):
	rooms = ChatRoom.objects.all()
	return render(request, "chat/chatroom_list.html", {"rooms": rooms})

@login_required
def chat_room(request, chatroom_name):
	room = get_object_or_404(ChatRoom, name=chatroom_name)
	return render(request, "chat/chat_room.html", {"room": room})
