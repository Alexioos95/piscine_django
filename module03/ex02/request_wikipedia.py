import dewiki
import json
import requests
import sys

API_URL = "https://en.wikipedia.org/w/api.php"

def get_title(query):
	params = {
		"action": "query",
		"list": "search",
		"srsearch": query,
		"format": "json"
	}
	response = requests.get(API_URL, params=params)
	if response.status_code != 200:
		print(f"Error {response.status_code}")
		return None
	data = response.json()
	try:
		res = data['query']['searchinfo']['suggestion']
		return res
	except:
		return None

def get_article(query):
	params = {
		"action": "query",
		"prop": "extracts",
		"titles": query,
		"explaintext": True,
		"format": "json"
	}
	response = requests.get(API_URL, params=params)
	if response.status_code != 200:
		print(f"Error {response.status_code}")
		return None
	data = response.json()
	pages = data.get("query", {}).get("pages", {})
	for page_id, page_data in pages.items():
		if "extract" in page_data:
			return dewiki.from_string(page_data["extract"])
	return None

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"Usage: python3 request_wikipedia.py <article_name>")
	else:
		title = get_title(sys.argv[1])
		if title == None:
			print(f"Error: No results found for '{sys.argv[1]}'.")
			exit(1)
		article = get_article(title)
		if article == None:
			print(f"Error: No article page found for '{title}'.")
			exit(1)
		file = f'{sys.argv[1].replace(" ", "_")}.wiki'
		with open(file, "w") as f:
			f.write(article)
