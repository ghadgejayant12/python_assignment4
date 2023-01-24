class VoterUnderAgeException(Exception):
	pass

class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.vote_done=False
		pass

	def cast_vote(self):
		if self.age<18:
			raise VoterUnderAgeException('The voter '+self.name+' is under age and cannot vote')
		else:
			self.vote_done=True
			print('The voter',self.name,'is of age',self.age,'and has casted the vote')

choose='y'
while choose=='y' or choose=='Y':
	name=input('Enter the name : ')
	age=int(input('Enter the age : '))
	p = Person(name,age)
	try:
		p.cast_vote()
	except VoterUnderAgeException as e:
		print(e)
	choose=input('Do you wish to continue (y/n) ?')