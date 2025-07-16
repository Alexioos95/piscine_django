def my_var():
	values = [
		42,
		"42",
		"quarante-deux",
		42.0,
		True,
		[42],
		{42: 42},
		(42,),
		set()
	]
	for value in values:
		print(f"{value} has a type {type(value)}")

if __name__ == '__main__':
	my_var()
