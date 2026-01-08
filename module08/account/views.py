from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.shortcuts import render

def account_view(request):
	return render(request, "account/account.html")

def ajax_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return JsonResponse({"success": True, "username": user.username})
		else:
			return JsonResponse({"success": False, "errors": form.errors})
	return JsonResponse({"success": False, "error": "Invalid request method"})

def ajax_logout(request):
	if request.method == "POST":
		logout(request)
		return JsonResponse({"success": True})
	return JsonResponse({"success": False, "error": "Invalid request method"})
