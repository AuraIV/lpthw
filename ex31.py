print "You enter a dark room with three doors. Do you go through door #1, door #2 or door #3?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating cheese cake! What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at the Cthulhu's retina"
	print "1. Blueberries."
	print "2. Yellow jacket clothespins. "
	print "3. Understanding revolvers yelling melodies"
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else: 
		print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
	print "You are outside in a starry night with a box in front of you. What do you do?"
	print "1. Pick it up and open it."
	print "2. Let it be"
	
	honesty = raw_input("> ")
	if honesty == 1:
		print "A cat comes out and scratches your face. Yikes."
	elif honesty == 2:
		print "You get home safely!"
	else:
		print "HUH... you sure you should do %s?" % honesty 

else:
	print "You stumble around and fall on a knife and die. YAY..?"
	
	