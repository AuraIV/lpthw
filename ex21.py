def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def substract(a, b):
	print "SUBSTRACTING %d - %d" % (a, b)
	return a - b 

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b 

def puzzle(a, b, c, d):
	return a + b - c * (d/2)

print "Let's do some math with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply (90, 2)
iq = divide(100, 2)

print "Age %d, Height %d, Weight %d, IQ %d." % (age, height, weight, iq)

#A Puzzle for extra credit:)
print "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

#age + height - weight * (iq/2)

what_two = puzzle(age, height, weight, iq)


print "That becomes: ", what, "Can you do it by hand?"
print "Did we solve the puzzle? %d" % what_two