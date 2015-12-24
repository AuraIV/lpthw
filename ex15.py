from sys import argv

script, filename = argv #takes the filename from the command line

txt = open(filename) #open the file given

print "Here's your file %r: " % filename
print txt.read #reads contents of the file
txt.close() #closes the file

print "Type the filename again:"
file_again = raw_input("> ") #prompts the user for the filename

txt_again = open(file_again) #open the file given
print txt_again.read() #reads contents of the file
txt_again.close() #closes the file

#The benefit of using raw_input is that the user gets
#prompted so if you don't know what the program does. It will help.