from django.shortcuts import render, redirect
from .models import MyUser, Tip
from .forms import RegisterForm, LoginForm, TipForm

def index(request):
	user_id = request.session.get("user_id")
	user = MyUser.objects.get(id=user_id) if user_id else None

	if request.method == "POST":
		form = TipForm(request.POST)
		if form.is_valid() and user != None:
			tip = form.save(commit=False)
			tip.author = user
			tip.save()
			return redirect("/ex02/")
	else:
		form = TipForm() if user else None
	tips = Tip.objects.all().order_by("-date")
	return render(request, "ex02/index.html", {"form": form, "tips": tips, "user": user})

def register(request):
	if request.session.get("user_id"):
		return redirect("/ex02/")
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = MyUser(
				username=form.cleaned_data["username"],
				password= form.cleaned_data["password"]
			)
			user.save()
			return redirect("/ex02/login")
		else:
			return render(request, "ex02/register.html", {"form": form})
	else:
		form = RegisterForm()
		return render(request, "ex02/register.html", {"form": form})

def login(request):
	if request.session.get("user_id"):
		return redirect("/ex02/")
	if request.method == "POST":
		form = LoginForm(request.POST)
		error = None
		if form.is_valid():
			try:
				user = MyUser.objects.get(username=form.cleaned_data["username"])
				if user.password == form.cleaned_data["password"]:
					request.session["user_id"] = user.id
					request.session["username"] = form.cleaned_data["username"]
					return redirect("/ex02/")
				else:
					error = "Incorrect password"
			except:
				error = "User not found"
			return render(request, "ex02/login.html", {"form": form, "error": error})
		else:
			return render(request, "ex02/login.html", {"form": form})
	else:
		form = LoginForm()
		return render(request, "ex02/login.html", {"form": form, "error": None})

def logout(request):
	request.session.flush()
	return redirect("/ex02/")
