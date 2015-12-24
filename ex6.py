x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
#Assigns binary and do not into this string for y 1
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y 

#Print x within this print 2
print "I said: %r." % x 
#Prints y within this print 3
print "I also said: '%s'." % y 

hilarious = False 

#sets a string that receives anything
joke_evaluation = "Isn't that joke so funny?! %r"

#you pass hilarius to the joke_evaluation  4
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e