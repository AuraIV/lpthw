from sys import argv
from os.path import exists 

script, from_file, to_file = argv 

print "Copying from %s to %s" % (from_file, to_file)

indata = (open(from_file)).read()

#print "The input file is %d bytes long" % len(indata) Not needed

#print "Does the output file exist? %r" % exists(to_file) Not needed
#print "Ready, hit RETURN to continue, CTRl-C to abort." Not needed
#raw_input() Not needed

outdata = (open(to_file, 'w')).write(indata) #truncates and opens and copies data
#into the new file

#out_file.write(indata) #copies the data to the new file

print "Alright, all done :)."

#out_file.close() #We opened the file to copy into, we need to close it now!

#We could write this like this, but I think it takes out readibility:
# (open(to_file, 'w')).write((open(from_file)).read())
