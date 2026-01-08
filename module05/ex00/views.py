from django.http import HttpResponse
from django.conf import settings
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
			CREATE TABLE IF NOT EXISTS ex00_movies (
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
