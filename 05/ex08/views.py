from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
import psycopg2
import csv
import os

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
			CREATE TABLE IF NOT EXISTS ex08_planets (
				id SERIAL PRIMARY KEY,
				name VARCHAR(64) UNIQUE NOT NULL,
				climate VARCHAR,
				diameter INTEGER,
				orbital_period INTEGER,
				population BIGINT,
				rotation_period INTEGER,
				surface_water REAL,
				terrain VARCHAR(128)
			);
			CREATE TABLE IF NOT EXISTS ex08_people (
				id SERIAL PRIMARY KEY,
				name VARCHAR(64) UNIQUE NOT NULL,
				birth_year VARCHAR(32),
				gender VARCHAR(32),
				eye_color VARCHAR(32),
				hair_color VARCHAR(32),
				height INTEGER,
				mass REAL,
				homeworld VARCHAR(64) REFERENCES ex08_planets(name)
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
	try:
		db = psycopg2.connect(
			dbname=settings.DATABASES["default"]["NAME"],
			user=settings.DATABASES["default"]["USER"],
			password=settings.DATABASES["default"]["PASSWORD"],
			host=settings.DATABASES["default"]["HOST"],
			port=settings.DATABASES["default"]["PORT"],
		)
		cursor = db.cursor()
		with open(os.path.join(settings.BASE_DIR, "ex08", "data", "planets.csv"), newline="") as f:
			fields = ["name", "climate", "diameter", "orbital_period", "population", "rotation_period", "surface_water", "terrain"]
			content = csv.DictReader(f, delimiter='\t', fieldnames=fields)
			for row in content:
				print(row)
				try:
					cursor.execute("""
						INSERT INTO ex08_planets (name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
						VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
					""", (
						row["name"],
						row["climate"] or None,
						int(row["diameter"]) if row["diameter"].isdigit() else None,
						int(row["orbital_period"]) if row["orbital_period"].isdigit() else None,
						int(row["population"]) if row["population"].isdigit() else None,
						int(row["rotation_period"]) if row["rotation_period"].isdigit() else None,
						float(row["surface_water"]) if row["surface_water"] != "NULL" else None,
						row["terrain"] or None,
					))
					db.commit()
					res.append("OK")
				except Exception as e:
					db.rollback()
					res.append(f"Error: {e}")
		res.append("---")
		with open(os.path.join(settings.BASE_DIR, "ex08", "data", "people.csv"), newline="") as f:
			fields = ["name", "birth_year", "gender", "eye_color", "hair_color", "height", "mass", "homeworld"]
			content = csv.DictReader(f, delimiter='\t', fieldnames=fields)
			for row in content:
				try:
					cursor.execute("""
						INSERT INTO ex08_people (name, birth_year, gender, eye_color, hair_color, height, mass, homeworld)
						VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
					""", (
						row["name"],
						row["birth_year"] or None,
						row["gender"] or None,
						row["eye_color"] or None,
						row["hair_color"] or None,
						int(row["height"]) if row["height"].isdigit() else None,
						float(row["mass"]) if row["mass"] != "NULL" else None,
						row["homeworld"] or None,
					))
					db.commit()
					res.append("OK")
				except Exception as e:
					db.rollback()
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
		cursor.execute("""
			SELECT people.name, people.homeworld, planet.climate
			FROM ex08_people AS people
			JOIN ex08_planets AS planet ON people.homeworld = planet.name
			WHERE planet.climate ILIKE '%windy%'
			ORDER BY people.name ASC;
		""")
		rows = cursor.fetchall()
		cursor.close()
		db.close()
		if not rows:
			return HttpResponse("No data available")
		return render(request, "ex08/index.html", {"data": rows})
	except Exception as e:
		return HttpResponse(f"Error: {e}")
