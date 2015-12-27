
numbers = []
numbers_two = []
numbers_three = []

def fillList(max, increments, list):
	"""Populates a list from 0 to max, with increments inputed, to the list given. """
	i = 0
	while i < max: 
		
		if increments == 0: #Will this create an infinte loop? Stop it.
			print "Uh oh! Infinite loop."
			return 
			
		print "at the top i is %d" % i 
		list.append(i)
		i += increments
		print "Numbers now: ", numbers 
		print "At the bottom i is %d" % i 
		
def fillListFor(max, list):
	"""Populates a list from 0 to max to the list given """
	for n in range (0, max):
		list.append(n)
		print "Numbers now: ", numbers 
		print "At the bottom i is %d" % n

fillList(6, 1, numbers)
fillList(8, 0, numbers_two)
fillListFor(6, numbers_three)
	
print "The numbers: "

for num in numbers:
	print num 
	
#Because we use range, we want to avoid the incrementor. 
#The range will go that amount of times no matter what. 
#so if you left the increment you will not have the desired effect