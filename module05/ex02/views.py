from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
import psycopg2

def init(request):
	try:
		db = psycopg2.connect(
			dbname=settings.DATABASES["default"]["NAME"],
			user=settings.DATABASES["default"]["USER"],
			password=settings.DATABASES["default"]["PASSWORD"],
			host=settings.DATABASES["default"]["HOST"],
			port=settings.DATABASES["default"]["PORT"],
		)
		cursor = db.cursor()
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS ex02_movies (
				episode_nb INTEGER PRIMARY KEY,
				title VARCHAR(64) UNIQUE NOT NULL,
				opening_crawl TEXT,
				director VARCHAR(32) NOT NULL,
				producer VARCHAR(128) NOT NULL,
				release_date DATE NOT NULL
			);
		""")
		db.commit()
		cursor.close()
		db.close()
		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse(f"Error: {e}")

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
		db = psycopg2.connect(
			dbname=settings.DATABASES["default"]["NAME"],
			user=settings.DATABASES["default"]["USER"],
			password=settings.DATABASES["default"]["PASSWORD"],
			host=settings.DATABASES["default"]["HOST"],
			port=settings.DATABASES["default"]["PORT"],
		)
		cursor = db.cursor()
		for item in movies:
			try:
				cursor.execute("""
					INSERT INTO ex02_movies (episode_nb, title, opening_crawl, director, producer, release_date)
					VALUES (%s, %s, %s, %s, %s, %s)
				""", item)
				res.append("OK")
			except Exception as e:
				res.append(f"Error: {e}")
		db.commit()
		cursor.close()
		db.close()
	except Exception as e:
		return HttpResponse(f"Error: {e}")
	return HttpResponse("<br>".join(res))

def display(request):
	try:
		db = psycopg2.connect(
			dbname=settings.DATABASES["default"]["NAME"],
			user=settings.DATABASES["default"]["USER"],
			password=settings.DATABASES["default"]["PASSWORD"],
			host=settings.DATABASES["default"]["HOST"],
			port=settings.DATABASES["default"]["PORT"]
		)
		cursor = db.cursor()
		cursor.execute("SELECT * FROM ex02_movies")
		rows = cursor.fetchall()
		cursor.close()
		db.close()
		if not rows:
			return HttpResponse("No data available")
		return render(request, "ex02/index.html", {"data": rows})
	except Exception as e:
		return HttpResponse(f"Error: {e}")
