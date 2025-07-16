from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from ex05.models import Movies

def populate(request):
	res = []
	movies = [
		(1, "The Phantom Menace", "", "George Lucas", "Rick McCallum", "1999-05-19"),
		(2, "Attack of the Clones", "", "George Lucas", "Rick McCallum", "2002-05-16"),
		(3, "Revenge of the Sith ", "", "George Lucas", "Rick McCallum", "2005-05-19"),
		(4, "A New Hope", "", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
		(5, "The Empire Strikes Back", "", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
		(6, "Return of the Jedi", "", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
		(7, "The Force Awakens", "", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
	]
	try:
		for item in movies:
			try:
				movie = Movies(*item)
				movie.save()
				res.append("OK")
			except Exception as e:
				res.append(f"Error: {e}")
	except Exception as e:
		return HttpResponse(f"Error: {e}")
	return HttpResponse("<br>".join(res))

def display(request):
	try:
		rows = Movies.objects.values_list('episode_nb', 'title', 'opening_crawl', 'director', 'producer', 'release_date')
		if not rows:
			return HttpResponse("No data available")
		return render(request, "ex05/index.html", {"data": rows})
	except Exception as e:
		return HttpResponse(f"Error: {e}")

def remove(request):
	try:
		if request.method == "POST":
			title = request.POST.get("title")
			movie = Movies.objects.get(title=title)
			movie.delete()
		rows = Movies.objects.values_list('episode_nb', 'title', 'opening_crawl', 'director', 'producer', 'release_date')
		return render(request, "ex05/form.html", {"data": rows})
	except Exception as e:
		return HttpResponse(f"Error: {e}")
