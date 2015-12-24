from sys import argv #import. Adds modules to your script. 

script, first, second, third = argv #Assign each thing to these variables

print "The script is called:", script
print "Your first variable is:", first 
print "Your second variable is:", second
print "Your thrid variable is:", third
fourth = raw_input("Fourth? ") #Addedd to combine argv and raw_input :)

#ValueError You need at least the amount of unpacked argv in your command line
#to not get an error!

