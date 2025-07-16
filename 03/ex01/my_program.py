import path

if __name__ == "__main__":
	try:
		folder = "./my_folder"
		path.Path(folder).mkdir()
		file = f'{folder}/my_file.txt'
		write_content = "Useless content text\n"
		with open(file, "w") as f:
			f.write(write_content)
		with open(file, "r") as f:
			read_content = f.read()
		print(f"File content: {read_content}")
	except Exception as e:
		print(f"Error: {e}")
