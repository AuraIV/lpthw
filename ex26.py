def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): #added a colon
    """Prints the first word after popping it off."""
    word = words.pop(0) #Fixed from poop to pop
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #Added a missing parenthesis
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6 #Changed five to six 
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #changed from a  \ to a /
    crates = jars / 100 
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) #fixed - to _, removed extra = 

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) #added an i to start_point and closed parenthesis


sentence = "All good things come to those who wait." #Fixed typos

words = break_words(sentence) #Removed references to ex25 
sorted_words = sort_words(words) #Removed references to ex25

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) #removed a period
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence) #Removed reference to ex25
print sorted_words #added a t

print_first_and_last(sentence) #added a i

print_first_and_last_sorted(sentence) #fixed typos
