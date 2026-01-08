import sys
import os
import re

def render(f, d, html):
	try:
		# base html
		html_content = f"""<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>{d["title"]}</title>
	</head>
	<body>
"""
		# read f and fill html's body
		for line in f:
			html_content += line.format(**d)
		# closing base html
		html_content += """	</body>
</html>"""
		html.write(f"{html_content}")

	except Exception as e:
		print(f"Error: {e}.")
	
if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Error: Wrong number of argument. Usage: python3 render.py <file>.template")
	elif (len(sys.argv[1]) < len("a.template") or sys.argv[1].find(".template", len(sys.argv[1]) - len(".template")) == -1):
		print("Error: The argument must be a .template file. Usage: python3 render.py <file>.template")
	else:
		try:
			# vars
			f = open(sys.argv[1], "r")
			sf = open("./settings.py")
			html = open(sys.argv[1].removesuffix(".template") + ".html", "w")
			d = {}
			exec(sf.read(), {}, d)
			# render
			render(f, d, html)
		except Exception as e:
			print(f"Error: {e}.")
