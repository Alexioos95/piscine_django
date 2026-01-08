class HotBeverage:
	def __init__(self, Price=None, Name="hot beverage"):
		self.Price = Price
		self.Name = Name
		if Price is None:
			self.Price = 0.30
		if Name is None:
			self.Name = "hot beverage"
	def description(self):
		return ("Just some hot water in a cup.")
	def __str__(self):
		return (f"name : {self.Name}\nprice : {self.Price}\ndescription : {self.description()}")

class Coffee(HotBeverage):
	def __init__(self):
		HotBeverage.__init__(self, 0.40, "coffee")
	def description(self):
		return ("A coffee, to stay awake.")

class Tea(HotBeverage):
	def __init__(self):
		HotBeverage.__init__(self, None, "tea")

class Chocolate(HotBeverage):
	def __init__(self):
		HotBeverage.__init__(self, 0.50, "chocolate")
	def description(self):
		return ("Chocolate, sweet chocolate...")

class Cappuccino(HotBeverage):
	def __init__(self):
		HotBeverage.__init__(self, 0.45, "cappuccino")
	def description(self):
		return ("Un po' di Italia nella sua tazza!")

if __name__ == '__main__':
	hot = HotBeverage()
	coffee = Coffee()
	tea = Tea()
	chocolate = Chocolate()
	cappuccino = Cappuccino()
	print(hot.__str__())
	print("\n")
	print(coffee.__str__())
	print("\n")
	print(tea.__str__())
	print("\n")
	print(chocolate.__str__())
	print("\n")
	print(cappuccino.__str__())
