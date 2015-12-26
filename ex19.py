from sys import argv
script, arg1, arg2 = argv

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackeers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

def adele (song):
	print "Hello, it's me. Singing %r" % song
	
print "We can just give the function numbers directly: "
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can do math inside too: "
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math!"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)

print "Oh! What does the user want?"
cheese = int(raw_input("How much cheese? "))
crackers = int(raw_input ("How many crackers? "))
cheese_and_crackers(cheese, crackers)

print "What about argv?"
other_cheese = int(arg1)
other_crackers = int(arg2)

cheese_and_crackers(other_cheese, other_crackers)

print "Now my own function!"
adele("Hello")

#Skipping #3 running it 10 different ways - added to cheese and crackers instead