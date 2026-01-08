from django.http import HttpResponse
from django.shortcuts import render
from .models import Planets, People

def display(request):
	rows = People.objects.select_related("homeworld").filter(homeworld__climate__icontains="windy")
	if not rows.exists():
		err = "No data available, please use the following command line before use:\npython3 manage.py loaddata ./ex09/data/ex09_initial_data.json"
		return HttpResponse(err.replace("\n", "<br>"))
	return render(request, "ex09/index.html", {"data": rows})
