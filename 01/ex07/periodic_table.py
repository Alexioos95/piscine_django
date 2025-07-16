def createTable(d):
	table = [
		["<tr>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "</tr>"],
	]
	line = 0
	prevIndex = 0
	for key, value in d.items():
		index = value["position"] + 1
		if index > 18:
			continue
		if prevIndex > index:
			line += 1
			table.append(["<tr>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "<td></td>", "</tr>"])
		table[line][index] = f"""
			<td>
				<h4>{key}</h4>
				<ul>
					<li>{value["number"]}</li>
					<li>{value["small"]}</li>
					<li>{value["molar"]}</li>
					<li>{value["electron"]}</li>
				</ul>
			</td>
		"""
		prevIndex = index
	res = "\n".join("".join(row) for row in table)
	return (res)

def periodic_table():
	# file
	file_path = "periodic_table.txt"
	with open(file_path, "r") as file:
		tab = []
		line = file.readline()
		while line:
			tab.append(line)
			line = file.readline()
	# tab to dict
	d = {}
	for line in tab:
		element, attributes = line.split(" = ")
		attributes_list = attributes.split(", ")
		element_dict = {}
		for pair in attributes_list:
			key, value = pair.split(":")
			if value.replace('.', '', 1).isdigit():
				value = float(value) if '.' in value else int(value)
			else:
				value = value
			element_dict[key] = value
		d[element] = element_dict
	# css
	css_style = """<style>
			html, body {
				width: 100%;
				height: 100%;
				margin: 0;
			}
			table {
				border-collapse: collapse;
			}
			th, td {
				min-width: 100px;
				min-height: 100px;
				border: 1px solid black;
				padding: 4px;
				text-align: center;
			}
		</style>"""
	# html
	html_dom = f"""<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Periodic Table</title>
		{css_style}
	</head>
	<body>
		<table>"""
	html_dom += createTable(d)
	html_dom += """
		</table>
	</body>
</html>"""
	with open("periodic_table.html", "w") as file:
		file.write(html_dom)

if __name__ == '__main__':
	periodic_table()
