# Study Drills

# Go through this program and write a comment above each line explaining it.
# Find all the places where a string is put inside a string. There are four places.
# Are you sure there are only four places? How do you know? Maybe I like lying.
# Explain why adding the two strings w and e with + makes a longer string.

# Lines 9 - 12 are difining variables and using "%d" to insert a value into a print statement.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who know %s." % (binary, do_not)
# Lines 14 & 15 are printing the "x, y" definitions.
print x
print y
# Lines 17 and 18 are printing a sentence and using "%r" to read the value of "x, y"
print "I said: %r." % x
print "I also said: %s . " % y
# Line 20 gives "Hilarious" a value of "False"
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# Line 23 asks is the joke was infact Hilarious.
print joke_evaluation % hilarious 
# Line 25 & 26 are defining "w & e"
w = "This is the left side of..."
e = "a string with a right side."
# Line 28 is adding "w + e"
print w + e
# In line 28 adding w + e makes the string longer because it is adding the two print 
#together.
