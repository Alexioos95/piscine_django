class Intern:
	def __init__(self, Name="My name? I'm nobody, an intern, I have no name."):
		self.Name = Name
	def __str__(self):
		return (self.Name)
	def work(self):
		raise Exception("I'm just an intern, I can't do that...")
	def make_coffee(self):
		return (Coffee())

class Coffee:
	def __str__(self):
		return ("This is the worst coffee you ever tasted.")

if __name__ == '__main__':
	nameless = Intern()
	mark = Intern("Mark")
	print(nameless.__str__())
	print(mark.__str__())
	print(mark.make_coffee())
	try:
		nameless.work()
	except Exception as e:
		print(f"Error: {e}")
