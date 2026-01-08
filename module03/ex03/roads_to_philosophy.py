import sys
import requests
from bs4 import BeautifulSoup

def get_link(url):
	try:
		response = requests.get(url)
		if response.status_code != 200:
			print(f"Error {response.status_code}")
			return None
		soup = BeautifulSoup(response.text, "html.parser")
		wrapper = soup.find("div", class_="mw-content-ltr")
		for p in wrapper.find_all("p"):
			for a in p.find_all("a", href=True):
				href = a.get("href")
				if "#" in href:
					continue
				elif href.startswith("/wiki/Help:") or href.startswith("/wiki/Special:") or href.startswith("/wiki/File:"):
					continue
				elif href.startswith("/wiki/"):
					return "https://en.wikipedia.org" + href
		return None
	except Exception as e:
		print(f"Error: {e}")
		return None

def pathing(query):
	url = "https://en.wikipedia.org/wiki/" + query.replace(" ", "_")
	article = query
	visited = []

	while url != None:
		if url in visited:
			print("It leads to an infinite loop!")
			return
		visited.append(url)
		print(f"{article}")
		if "Philosophy" in url:
			print(f"{len(visited)} roads from {query} to Philosophy")
			return
		next = get_link(url)
		if next == None:
			print("It leads to a dead end!")
			return
		url = next
		article = url[30:].replace("_", " ")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 ./roads_to_philosophy.py <article_name>")
	else:
		pathing(sys.argv[1])
