# Study Drills

# This is a big jump so be sure you do this Study Drill as best you can before moving on.

# Above each line, write out in English what that line does.
# If you are not sure ask someone for help or search online. 
# Many times searching for "python THING" will find answers for what that THING does in Python. 
# Try searching for "python open."
# I used the name "commands" here, but they are also called "functions" and "methods." 
# Search around online to see what other people do to define these. 
# Do not worry if they confuse you. It's normal for programmers to confuse you with their vast extensive knowledge.
# Get rid of the part from lines 10-15 where you use raw_input and try the script then.
# Use only raw_input and try the script that way. 
# Think of why one way of getting the filename would be better than another.
# Run pydoc file and scroll down until you see the read() command (method/function). 
# See all the other ones you can use? Skip the ones that have __ (two underscores) in front 
# because those are junk. Try some of the other commands.
# Start python again and use open from the prompt. 
# Notice how you can open files and run read on them right there?
# Have your script also do a close() on the txt and txt_again variables. 
# It's important to close files when you are done with them.
#-----------------------------------------------------------------------------------
#Line 24 is saying that you import the argv list from the sys module. 
from sys import argv
# Line 26 is running the script filename = argv
script, filename = argv
# Line 28 saying open txt document
txt = open(filename)
# Line 30 is giving you the file
print "Here's your file %r:" % filename
# Line 32 is saying print the contents of txt.read()
print txt.read()
# Line 34 is asking you to print the file name again
print "Type the filename again:"
# Line 36 is asking for your input
file_again = raw_input("> ")
# Line 38 is telling the computer to open the file again
txt_again = open(file_again)
# Line 40 is reading the contents of the file again
print txt_again.read()
# I am inserting a close() finction to close the text file. 
print "Let's close the file."
txt.close()


