from sys import argv

script, filename = argv

print "Here's your file: %r\n" % filename 
txt = open(filename)
print txt.read()
txt.close()