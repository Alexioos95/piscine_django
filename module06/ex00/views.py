from django.shortcuts import render
from django.http import JsonResponse

def index(request):
	return render(request, "ex00/index.html")

def get_username(request):
	username = request.session.get("username")
	return JsonResponse({"username": username})
