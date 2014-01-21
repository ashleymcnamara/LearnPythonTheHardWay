# Study Drills

# Go read up on Python's import statement, and start python to try it out. 
# Try importing some things and see if you can get it right. It's alright if you do not.
# This script is really annoying. There's no need to ask you before doing the copy, 
# and it prints too much out to the screen. Try to make it more friendly to use by 
# removing features.
# See how short you can make the script. I could make this one line long.
# Notice at the end of the WYSS I used something called cat?
# It's an old command that "con*cat*enates" files together, 
# but mostly it's just an easy way to print a file to the screen. Type man cat to read about it.
# Windows people, find the alternative to cat that Linux/OSX people have. 
# Do not worry about man since there is nothing like that.
# Find out why you had to do output.close() in the code.
#--------------------------------------------------------------------------------------------- 
#
# Original Script 
#
from sys import argv
# Line 22, This returns True if a file exists, based on its name in a string as an argument.
# It returns False if not. 
from os.path import exists
# Line 24 is creating the script, saying take information from this file and apply it to this file.
script, from_file, to_file = argv
# Line 26 is printing a statement telling the user that the script is transfering content from one file to the next.
print "Copying from %s to %s" % (from_file, to_file)
# Lines 28-29 are opening the txt file and reading the text file. You can shorten it to
# One line by using ; in between functions. 
in_file = open(from_file);
indata = in_file.read()
# Line 32 is telling the user how many bytes the file is.
print "The input file is %d bytes long" % len(indata)
# Line 34 is asking a True or False question. Does the file exist? If so get the file.
print "Does the output file exist? %r" % exists(to_file)
# Line 36 is asking the userif they want to procede with the action or not. 
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
# Lines 40-41 are opening the file and saying, "I am going to write to this file."
# but it's taking the contents from the first txt file and putting it onto the second.
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."
# Lines 46-46 are closing both files.
out_file.close()
in_file.close()
#
#------------------------------------------------------------------------------------------
#
# Updated Script
#
# I am sure there is a better way but this is how I got rid of all of the fluff and got all of
# the code onto one line. 
ffrom sys import argv
from os.path import exists

script, from_file, to_file = argv; in_file = open(from_file); indata = in_file.read(); out_file = open(to_file, 'w'); out_file.write(indata); out_file.close(); in_file.close() 

