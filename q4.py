# Create a program to check eligibility of the person for loan  with the help of oops concepts and exception handling.
# Person whose salary is less than 10K/ Month will not be eligible for the loan

class LoanNotEligibleException(Exception):
	def __str__(self):
		return 'This person is not eligle to apply for loan'
	pass

class Person:
	def __init__(self,name,company,salary):
		self.name=name
		self.company=company
		self.salary=salary
		self.loan=None 

	def get_loan(self,amount):
		if self.salary<10000:
			raise LoanNotEligibleException
		else:
			self.loan=amount
			print(name,'is eligible for loan of',amount)
	def __str__(self):
		return 'Name : '+str(self.name)+' Company : '+str(self.company)+' Salary : '+str(self.salary)

choose='y'
while choose=='y' or choose=='Y':
	name=input('Enter name : ')
	salary=int(input('Enter salary : '))
	company=input('Enter Company : ')
	p = Person(name,company,salary)
	ln = input('Does this person want a loan ? (y/n) : ')
	try:
		if ln=='y' or ln=='Y':
			p.get_loan(int(input('Enter amount of loan needed : ')))
	except LoanNotEligibleException as e:
		print(e)
	choose=input('Want to continue ? (y/n) : ')
	