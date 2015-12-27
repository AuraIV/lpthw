people = 30
cars = 40
trucks = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if trucks > cars: 
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else: 
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."
else: 
	print "Fine, let's stay home then."
	
#elif -> else if (if the first statement is false, and if this one is true)
#else if all the statements before are false then...

#For the comments, it's boolean logic! > is greater than, < less than :)