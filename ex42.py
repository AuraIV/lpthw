## Animal is-a object (yes, sort of consuing...)

class Animal(object):
	pass 
	
## Dog is-a Animal 
class Dog(Animal):
	def __init__(self, name):
		## has a name 
		self.name = name 

## Cat is-a Animal 
class Cat(Animal):
	def __init__(self, name):
		## Cat has-a name 
		self.name = name

## Person is-a object 
class Person(object):
	
	def __init__(self, name):
		## Person has-a name 
		self.name = name 
		self.friends = [] 
		## Person has-a pet 
		self.pet = None # default 
	
	def addFriend(self, friend): #Allows a person to have friends
		self.friends.append(friend)
	
	def printFriends(self):
		for f in self.friends: 
			print f.name 

## Employee is-a Person 
class Employee(Person):
	def __init__(self, name, salary):
		## Person has-a name; thus Employee has-a-name (inheritance)
		super(Employee, self).__init__(name)
		## Employee has a salary 
		self.salary = salary
	
## Fish is-a object 
class Fish(object):
	def __init__(self):
		self = self 
	def swim(self):
		print "Just keep swimming <3"

## Salmon is-a Fish 
class Salmon(Fish):
	pass

## Halibut is a fish
class Halibut(Fish):
	pass 

##Rover is-a Dog 
rover = Dog("Rover")

##Satan is a cat 
satan = Cat("Satan")

#Mary is a Person
mary = Person ("Mary")

## mary has-a pet which is-a Cat
mary.pet = satan 


## Frank is-a Employee who has-a Name and has-a salary
frank = Employee("Frank", 120000)

#frank is-a person who has-a pet 
frank.pet = rover #rover is-a dog 

mary.addFriend(frank) #YAY MARY HAS A FRIEND!!
mary.printFriends() #who is it again?

#flipper is-a Fish
flipper = Fish() 

## Crouse is-a Salmon
crouse = Salmon() 
crouse.swim() #Inherits the methods from fish :)
##harry is a halibut 
harry = Halibut() 
