print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you are %r old, %r tall and %r heavy." % (age, height, weight)

# Raw input take input as given into a string. 
#In Python 3 it was renamed Input(). In Python2 you do not use
# input() because of security issues

#The reason why you see a \' sequence in the print is because the format is raw.
# and since it did single quotes (there's a "), it attempted to print the ' with the sequence to escape
# but the raw printed the whole sequence. 

#Another simple form testing a different format string
print "How you doin?"
mood = raw_input()

print ("Huh, cool that you are %s") % (mood)