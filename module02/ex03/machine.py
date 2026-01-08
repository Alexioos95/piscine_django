import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
	def __init__(self):
		self.service = 10
		self.rand = 0 if random.randint(1, 100) % 2 == 0 else 1

	class EmptyCup(HotBeverage):
		def __init__(self):
			HotBeverage.__init__(self, 0.90, "empty cup")
		def description(self):
			return ("An empty cup?! Gimme my money back!")

	class BrokenMachineException(Exception):
		def __init__(self):
			Exception.__init__(self, "This coffee machine has to be repaired.")

	def repair(self):
		self.service = 10
	
	def serve(self, beverage):
		if (self.service == 0):
			raise self.BrokenMachineException()
			return
		self.service -= 1
		print(f"serving {beverage.description()}")
		if (self.rand == 0):
			self.rand = 1
			return (beverage)
		else:
			self.rand = 0
			return (self.EmptyCup())

if __name__ == '__main__':
	# Machine
	machine = CoffeeMachine()
	# Beverage
	hot = HotBeverage()
	coffee = Coffee()
	tea = Tea()
	chocolate = Chocolate()
	cappuccino = Cappuccino()
	# Serving
	print(f"{machine.serve(hot)}\n")
	print(f"{machine.serve(hot)}\n")
	print(f"{machine.serve(coffee)}\n")
	print(f"{machine.serve(coffee)}\n")
	print(f"{machine.serve(tea)}\n")
	print(f"{machine.serve(tea)}\n")
	print(f"{machine.serve(chocolate)}\n")
	print(f"{machine.serve(chocolate)}\n")
	print(f"{machine.serve(cappuccino)}\n")
	print(f"{machine.serve(cappuccino)}\n")
	# Not working
	try:
		print(f"{machine.serve(hot)}\n")
	except Exception as e:
		print(f"Error: {e}\n")
	# Repair
	machine.repair()
	# Serving
	print(f"{machine.serve(hot)}\n")
