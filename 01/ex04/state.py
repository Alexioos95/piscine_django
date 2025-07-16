import sys

def state():
	if len(sys.argv) != 2:
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
	# print
	arg = sys.argv[1]
	if arg in capital_cities.values():
		code = next((key for key, value in capital_cities.items() if value == arg), None)
		if code in states.values():
			name = next((key for key, value in states.items() if value == code), None)
			if name != None:
				print(name)
	else:
		print("Unknown capital city")

if __name__ == '__main__':
	state()
