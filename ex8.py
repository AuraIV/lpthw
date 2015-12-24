#stores four different things
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
#It prints the string formatter for times
print formatter % (formatter, formatter, formatter, formatter)
print formatter %(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing. ", 
	"So I said goodnight."
	)
	
	#The last line of output uses double quotes when the string inside contains a single quote