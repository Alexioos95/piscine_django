from django.shortcuts import render, redirect
from .models import MyUser
from .forms import RegisterForm, LoginForm

def index(request):
	return render(request, "ex01/index.html")

def register(request):
	if request.session.get("user_id"):
		return redirect("/ex01/")
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = MyUser(
				username=form.cleaned_data["username"],
				password=form.cleaned_data["password"]
			)
			user.save()
			return redirect("/ex01/login")
		else:
			return render(request, "ex01/register.html", {"form": form})
	else:
		form = RegisterForm()
		return render(request, "ex01/register.html", {"form": form})

def login(request):
	if request.session.get("user_id"):
		return redirect("/ex01/")
	if request.method == "POST":
		form = LoginForm(request.POST)
		error = None
		if form.is_valid():
			try:
				user = MyUser.objects.get(username=form.cleaned_data["username"])
				if user.password == form.cleaned_data["password"]:
					request.session["user_id"] = user.id
					request.session["username"] = form.cleaned_data["username"]
					return redirect("/ex01/")
				else:
					error = "Incorrect password"
			except:
				error = "User not found"
			return render(request, "ex01/login.html", {"form": form, "error": error})
		else:
			return render(request, "ex01/login.html", {"form": form})
	else:
		form = LoginForm()
		return render(request, "ex01/login.html", {"form": form, "error": None})

def logout(request):
	request.session.flush()
	return redirect("/ex01/")
