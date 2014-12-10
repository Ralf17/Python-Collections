#!/usr/bin/env python

class Dog():
	def __init__(self, dogname, dogcolor, dogheight, dogbuild, dogmood, dogage):
		self.name = dogname
		self.color = dogcolor
		self.height = dogheight
		self.build = dogbuild
		self.mood = dogmood
		self.age = dogage
		self.Hungry = False
		self.Tired = False
		
	def Eat(self):
		if self.Hungry:
			print 'Yum, yum ... num, num'
			self.Hungry = False
		else:
			print 'Sniff, sniff... not hungry'
			
	def Sleep(self):
		print 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
		self.Tired = False
		
	def Bark(self):
		if self.mood == 'Grumpy':
			print 'GRRRR... Woof Woof'
		elif self.mood == 'Laid Back':
			print 'Yawn...ok... Woof'
		elif self.mood == 'Crazy':
			print 'Bark Bark Bark Bark Bark Bark Bark Bark'
		else:
			print 'Woof Woof'
		
Beagle = Dog('Archie', 'Brown', 'Short', 'Chubby', 'Grumpy', 12)
print 'My name is %s' % Beagle.name
print 'My color is %s' % Beagle.color
print 'My mood is %s' % Beagle.mood	
print 'I am hungry = %s' % Beagle.Hungry
Beagle.Eat()	
Beagle.Hungry = True	
Beagle.Eat()	
Beagle.Bark()				
