# Study Drills

# If you feel you do not understand this, go back through and use the comment trick to 
# get it squared away in your mind. One simple English comment above each line will help you 
# understand or at least let you know what you need to research more.
# Write a script similar to the last exercise that uses read and argv to read the file you 
# just created.
# There's too much repetition in this file. Use strings, formats, and escapes 
# to print out line1, line2, and line3 with just one target.write() command instead of six.
# Find out why we had to pass a 'w' as an extra parameter to open.
# Hint: open tries to be safe by making you explicitly say you want to write a file.
# If you open the file with 'w' mode, then do you really need the target.truncate()?
# Go read the docs for Python's open function and see if that's true.
#-----------------------------------------------------------------------------------
# Import arguments from system.
from sys import argv
# Defines the arguments the system should grab.
script, filename = argv
# Line 20 is giving the user a choice, User, do you want to erase the file or not?
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# Line 24 takes the user's input and applies it.
raw_input("?")

print "Opening the file..."
# Line 28 opens the file and the 'w' is saying, 
# "When the file is open, we would like to write to this file." but the 'w' also wipes it clean.
target = open(filename, 'w')
# Line 30 is redundant, if you're already using 'w' then you don't need to truncate. 
print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
# Lines 35 - 37 are asking for the users input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write to the file."
# Lines 41-46 take that user's input and writes it to the txt file.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
# Then the file is closed.
target.close()
