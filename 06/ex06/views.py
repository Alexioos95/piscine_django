from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, TipForm
from django.http import HttpResponseForbidden
from .models import Tip, Vote
from ex04.models import MyUser
from django.contrib.auth import login
from django.http import Http404

def index(request):
	user = request.user if request.user.is_authenticated else None
	if request.method == "POST":
		form = TipForm(request.POST)
		if form.is_valid():
			tip = form.save(commit=False)
			tip.author = user
			tip.save()
			return redirect("index")
	else:
		form = TipForm() if user else None
	tips = Tip.objects.all().order_by("-date")
	return render(request, "ex06/index.html", {"form": form, "tips": tips, "user": user})

def register(request):
	if request.user.is_authenticated:
		return redirect("index")
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = MyUser.objects.create_user(
				username=form.cleaned_data["username"],
				password= form.cleaned_data["password"]
			)
			user.save()
			return redirect("login")
		else:
			return render(request, "ex06/register.html", {"form": form})
	else:
		form = RegisterForm()
		return render(request, "ex06/register.html", {"form": form})

def login_v(request):
	if request.user.is_authenticated:
		return redirect("index")
	if request.method == "POST":
		form = LoginForm(request.POST)
		error = None
		if form.is_valid():
			try:
				user = form.cleaned_data["user"]
				if user:
					login(request, user)
					return redirect("index")
				else:
					error = "Incorrect credentials"
			except:
				error = "User not found"
			return render(request, "ex06/login.html", {"form": form, "error": error})
		else:
			return render(request, "ex06/login.html", {"form": form})
	else:
		form = LoginForm()
		return render(request, "ex06/login.html", {"form": form, "error": None})

def logout(request):
	request.session.flush()
	return redirect("index")

def vote(request, id, type):
	if not request.user.is_authenticated:
		return redirect("login")
	tip = get_object_or_404(Tip, id=id)
	if type == "down":
		if request.user.has_perm("ex06.downvote_tip") or tip.author == request.user:
			vote, created = Vote.objects.get_or_create(
				user_id=request.user.id,
				tip=tip,
				defaults={"type": "down"}
			)
			if not created and vote.type == type:
				vote.delete()
			else:
				vote.type = type
				vote.save()
		else:
			return HttpResponseForbidden("You are not allowed to downvote this tip.")
	elif type == "up":
		vote, created = Vote.objects.get_or_create(
				user_id=request.user.id,
				tip=tip,
				defaults={"type": "up"}
			)
		if not created and vote.type == type:
			vote.delete()
		else:
			vote.type = type
			vote.save()
	else:
		raise Http404("Invalid vote type")
	return redirect("index")

def delete(request, id):
	if not request.user.is_authenticated:
		return redirect("login")
	tip = get_object_or_404(Tip, id=id)
	if request.user.has_perm("ex06.delete_tip") or tip.author == request.user:
		tip.delete()
		return redirect("index")
	else:
		return HttpResponseForbidden("You are not allowed to delete this tip.")
