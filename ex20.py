from sys import argv

script, input_file = argv

#prints the whole contents of the file
def print_all(f):
	print f.read()

#Makes the file point to absolute file positioning. (1st line)
def rewind(f):
	f.seek(0)

#Prints the line :)
def print_a_line(line_count, f):
	print line_count, f.readline()

#Opens the file
current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1 #Prints the first line
print_a_line(current_line, current_file)

current_line += 1 #current_line = 2
print_a_line(current_line, current_file)

current_line += 1 #current_line = 3
print_a_line(current_line, current_file)
