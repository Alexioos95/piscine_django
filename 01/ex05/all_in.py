import sys

def all_in():
	if len(sys.argv) != 2:
		return
	if ",," in sys.argv[1]:
		return
	# data
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	# format
	s = states.copy()
	cc = capital_cities.copy()
	for d in [s, cc]:
		d.update({key.lower(): value.lower() if isinstance(value, str) else value for key, value in d.items()})
	# print
	tab = sys.argv[1].split(", ")
	for og_search in tab:
		search = og_search.strip()
		search = search.lower()
		if len(search) == 0:
			continue
		elif search in s:
			code = s[search]
			if code in cc:
				print(f"{cc[code].title()} is the capital of {search.title()}")
		elif search in cc.values():
			code = next((key for key, value in cc.items() if value == search), None)
			if code in s.values():
				name = next((key for key, value in s.items() if value == code), None)
				if name != None:
					print(f"{search.title()} is the capital of {name.title()}")
		else:
			print(f"{og_search} is neither a capital city nor a state\r")

if __name__ == '__main__':
	all_in()
