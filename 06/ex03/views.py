from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, TipForm
from .models import MyUser, Tip, Vote
from django.http import Http404

def index(request):
	user_id = request.session.get("user_id")
	user = MyUser.objects.get(id=user_id) if user_id else None

	if request.method == "POST":
		form = TipForm(request.POST)
		if form.is_valid():
			tip = form.save(commit=False)
			tip.author = user
			tip.save()
			return redirect("/ex03/")
	else:
		form = TipForm() if user else None
	tips = Tip.objects.all().order_by("-date")
	return render(request, "ex03/index.html", {"form": form, "tips": tips, "user": user})

def register(request):
	if request.session.get("user_id"):
		return redirect("/ex03/")
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = MyUser(
				username=form.cleaned_data["username"],
				password= form.cleaned_data["password"]
			)
			user.save()
			return redirect("/ex03/login")
		else:
			return render(request, "ex03/register.html", {"form": form})
	else:
		form = RegisterForm()
		return render(request, "ex03/register.html", {"form": form})

def login(request):
	if request.session.get("user_id"):
		return redirect("/ex03/")
	if request.method == "POST":
		form = LoginForm(request.POST)
		error = None
		if form.is_valid():
			try:
				user = MyUser.objects.get(username=form.cleaned_data["username"])
				if user.password == form.cleaned_data["password"]:
					request.session["user_id"] = user.id
					request.session["username"] = form.cleaned_data["username"]
					return redirect("/ex03/")
				else:
					error = "Incorrect password"
			except:
				error = "User not found"
			return render(request, "ex03/login.html", {"form": form, "error": error})
		else:
			return render(request, "ex03/login.html", {"form": form})
	else:
		form = LoginForm()
		return render(request, "ex03/login.html", {"form": form, "error": None})

def logout(request):
	request.session.flush()
	return redirect("/ex03/")

def vote(request, id, type):
	if not request.session.get("user_id"):
		return redirect("/ex03/login")
	user_id = request.session["user_id"]
	tip = get_object_or_404(Tip, id=id)
	if type not in ["up", "down"]:
		raise Http404("Invalid vote type")
	vote, created = Vote.objects.get_or_create(user_id=user_id, tip=tip)
	if not created and vote.type == type:
		vote.delete()
	else:
		vote.type = type
		vote.save()
	return redirect("/ex03/")

def delete(request, id):
	tip = get_object_or_404(Tip, id=id)
	tip.delete()
	return redirect("/ex03/")
