# Create animal base class with attribute and related methods then create sub concrete subclass using animal eg of subclass: cow, horse, dog

class Animal:
	def __init__(self,name,kind):
		self.name=name
		self.kind=kind

	def move(self):
		print('This animal of type',self.kind,'having name ',self.name,'has moved')
		pass

	def eat(self):
		print('This animal of type',self.kind,'having name',self.name,'has eaten')
		pass

class Cow(Animal):
	def __init__(self,name,species,max_milk):
		super().__init__ (name,'Cow')
		self.species=species
		self.max_milk=max_milk
		self.milk_given=0
		pass

	def give_milk(self,qty):
		if self.milk_given>=self.max_milk:
			print('No more milk can be given by this cow')
			return
		print('This cow of species :',self.species,'has given',qty,'litres of milk')
		self.milk_given=self.milk_given+qty
		pass

class Horse(Animal):
	def __init__(self,name,species,max_miles):
		super().__init__(name,'Horse')
		self.species=species
		self.max_miles=max_miles
		self.miles_ran=0
		pass

	def run_miles(self,miles):
		if self.miles_ran>=self.max_miles:
			print('Horse cannot run anymore maximum miles reached')
			return
		print('This horse of species :',self.species,'has ran',miles,'.')
		self.miles_ran=self.miles_ran+miles
		pass

def main():
	print('Now Creating a horse')
	horse_name=input('Name of the Horse : ')
	horse_species=input('Species of the Horse : ')
	horse_max_miles=int(input('Maximum Horse can run in 1 day : '))
	horse = Horse(name=horse_name,species=horse_species,max_miles=horse_max_miles)
	choose='y'
	while choose=='y' or choose=='Y':
		print('1. Horse eats')
		print('2. Horse moves')
		print('3. Horse Runs')
		option=int(input('What should horse do ? : '))
		if option==1:
			horse.eat()
			pass
		elif option==2:
			horse.move()
			pass
		elif option==3:
			miles=int(input('How many miles horse should run ? : '))
			horse.run_miles(miles)
			pass
		else:
			print('Enter a valid choice')
		choose=input('Do you wish to continue ? (y/n) : ')
		pass
	print('--------------------------------------------------------------------')
	print('Now Creating a Cow')
	cow_name=input('Name of the cow : ')
	cow_species=input('Species of the cow : ')
	cow_max_milk=int(input('Maximum milk cow can give in 1 day : '))
	cow = Cow(name=cow_name,species=cow_species,max_milk=cow_max_milk)
	choose='y'
	while choose=='y' or choose=='Y':
		print('1. Cow eats')
		print('2. Cow moves')
		print('3. Cow gives milk')
		option=int(input('What should Cow do ? : '))
		if option==1:
			cow.eat()
			pass
		elif option==2:
			cow.move()
			pass
		elif option==3:
			qty=int(input('How much milk should cow give ? : '))
			cow.give_milk(qty)
			pass
		else:
			print('Enter a valid choice')
		choose=input('Do you wish to continue ? (y/n) : ')
main()
