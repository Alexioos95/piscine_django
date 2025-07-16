from django.db.models import Prefetch
from django.http import HttpResponse
from django.shortcuts import render
from .models import People, Movies
from ex10.forms import Form

def index(request):
	res = []
	if request.method == "POST":
		form = Form(request.POST)
		if form.is_valid():
			min_date = form.cleaned_data["min_date"]
			max_date = form.cleaned_data["max_date"]
			min_diameter = form.cleaned_data["min_diameter"]
			gender = form.cleaned_data["gender"]

			movies = Movies.objects.filter(release_date__range=(min_date, max_date))
			res = People.objects.select_related("homeworld").prefetch_related(Prefetch("movies_set", queryset=movies, to_attr="filtered_movies")).filter(
				gender=gender,
				homeworld__diameter__gt=min_diameter,
				movies__in=movies
			).distinct()
		else:
			res = None
	else:
		form = Form()
		res = None
	return render(request, "ex10/form.html", {"form": form, "data": res})
