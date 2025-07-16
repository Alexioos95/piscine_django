def numbers():
	file_path = "numbers.txt"
	with open(file_path, "r") as file:
		file_str = ""
		line = file.readline()
		while line:
			file_str += line
			line = file.readline()
	tab = file_str.split(",")
	for nb in tab:
		print(f"{nb}")

if __name__ == '__main__':
	numbers()
