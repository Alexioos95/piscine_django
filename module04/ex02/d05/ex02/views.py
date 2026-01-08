from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from .forms import Form
import os

def index(request):
	log_path = settings.LOG
	if not os.path.exists(log_path):
		with open(log_path, "w") as f:
			pass
	if request.method == "POST":
		form = Form(request.POST)
		if form.is_valid():
			input = form.cleaned_data["input"]
			time = datetime.now()
			log = f"{time}: {input}"
			with open(log_path, "a") as f:
				f.write(log + "\n")
	else:
		form = Form()
	with open(log_path, "r") as f:
		history = f.readlines()
	context = {
		"form": form,
		"history": history
	}
	return render(request, "ex02/index.html", context)
