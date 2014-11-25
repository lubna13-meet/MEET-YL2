class Animal():
	
	def __init__ (self, name, age):
		self.age=age
		self.name=name
	def sleep(self):
		print self.name +" "+ "of" + " " + str(self.age) + " " + "is sleeping"
	def eat(self, food):
		print self.name +" "+ "of" + " " + str(self.age) +" "+ "is eating" + " " + food

class Bird(Animal):
	def __init__ (self, name, age, wingcolor):
		Animal.__init__ (self, name, age)
		self.wingcolor = wingcolor
	def fly (self):
		print "Bird" + " " + self.name + " " + str(self.age) + " " + self.wingcolor
#	def __init__(self, name, age):
#		Animal.__init__ (self, name , age)
#	def bark(self):

		








x=Animal("MEET",11)
x.sleep()
y=Animal("Cat", 2)
y.sleep()
y.eat("pizza")
z=Animal("Dog", 3)
z.eat("apple")
l=Bird("lulu", 2, "blue")
l.fly()