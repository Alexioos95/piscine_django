import sys

def capital_city():
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
	if arg in states:
		code = states[arg]
		if code in capital_cities:
			print(capital_cities[code])
	else:
		print("Unknown state")

if __name__ == '__main__':
	capital_city()
