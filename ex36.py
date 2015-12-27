from sys import exit

def start():
	print "Hello, what's your name?"
	name = raw_input("> ")
	print "Well,", name, "you have two options: "
	print "Go left or right?"
	choice = raw_input("> ")
	if choice == "left":
		monster_room()
	elif choice == "right":
		beach_room()
	else:
		print "Ok I see how it is :(, bye %r" % name 
		dead()

def monster_room():
	weapons = ["Bow and arrow", "Wand", "Sword"]
	i = 1; #Counts the number of weapons
	print "Pick a weapon (Type it in) to fight of the evil kraken: "
	for weapon in weapons:
		print "%d. %r" % (i, weapon)
		i+=1
		
	choice = raw_input("> ")
	
	if choice == weapons[0]:
		print "Oh no, it's bouncing off the monster! Try again."
		monster_room()
	elif choice == weapons[1]:
		print "Oh yay! You beat it :)"
		beach_room()
	elif choice == weapons[2]:
		print "Wow, you're brave!"
		wins()
	else:
		dead()

def beach_room():
	print "You're at a beach, a crab offers you a drink. Do you take it?"
	choice = raw_input("> ")
	if choice == "Yes":
		print "The crab thinks you're super polite"
		wins()
	else:  
		print "The crab is annoyed."
		dead()

def dead():
	print "You died"
	exit(0)
	
def wins():
	print "Aw, congratulations! You've won"
	exit(0)

start()