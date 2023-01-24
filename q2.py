# Create arithmetics class to calculate avg, mean, mode and standard deviation
import math
class Arithmetics:
	def __init__(self,data):
		self.data=data
		self.avg=None
		self.mean=None
		self.mode=None
		self.standard_dev=None
		pass

	def do_avg(self):
		if self.avg!=None:
			return self.avg
		self.avg = sum(self.data)/len(self.data)
		return self.avg

	def do_mean(self):
		if self.mean!=None:
			return self.mean
		self.mean = sum(self.data)/len(self.data)
		return self.mean

	def do_mode(self):
		if self.mode!=None:
			return self.mode
		freq=dict()
		for i in self.data:
			if freq.get(i):
				freq[i]=freq[i]+1
			else:
				freq[i]=1
		max1=-1
		max_freq=-1
		for key,value in freq.items():
			if value>max_freq:
				max1=key
				max_freq=value
		self.mode=max1
		return max1

	def do_standard_dev(self):
		N = len(self.data)
		a=0
		for i in self.data:
			a=a+(i - self.mean)**2
		self.standard_dev=math.sqrt(a/N)
		return self.standard_dev

choose='y'
while choose=='y' or choose=='Y':
	nums=list(map(float,input('Enter the data : ').split()))
	calc = Arithmetics(data=nums)
	calc.do_avg()
	calc.do_mode()
	calc.do_mean()
	calc.do_standard_dev()
	print('The average calculated is :',calc.avg)
	print('The mode calculated is :',calc.mode)
	print('The standard deviation calculated is :',calc.standard_dev)
	choose=input('Do you want to continue (y/n) ? : ')