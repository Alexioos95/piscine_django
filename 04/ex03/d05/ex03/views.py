from django.shortcuts import render

def get_shades(rgb, nb_shades):
	r, g, b = rgb
	return [
		f"rgb({int(r * (1 - i / nb_shades))}, {int(g * (1 - i / nb_shades))}, {int(b * (1 - i / nb_shades))})"
		for i in range(1, nb_shades + 1)
	]

def index(request):
	shades = {
		"black": get_shades((0, 0, 0), 50),
		"red": get_shades((255, 0, 0), 50),
		"blue": get_shades((0, 0, 255), 50),
		"green": get_shades((0, 128, 0), 50),
	}
	data = list(zip(shades["black"], shades["red"], shades["blue"], shades["green"]))
	return render(request, "ex03/index.html", {"data": data})
