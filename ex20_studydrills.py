# Study Drills

# Go through and write English comments for each line to understand what's going on.
# Each time print_a_line is run, you are passing in a variable current_line. 
# Write out what current_line is equal to on each function call, and trace how it becomes line_count in print_a_line.
# Find each place a function is used, and go check its def to make sure that you are giving it the right arguments.
# Research online what the seek function for file does. Try pydoc file and see if you can figure it out from there.
# Research the shorthand notation += and rewrite the script to use that.
#----------------------------------------------------------------------------------------------
from sys import argv

script, input_file = argv
# Line 14, Print the entire file.
def print_all(f):
	print f.read()
# Line 17, Return to the top of the file.
def rewind(f):
	f.seek(0)
# Line 20, count the lines and read only the lines you tell it to.
def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)
# Line 25, printing a new file on a new line
print "First let's print the whole file:\n"
# Line 27, print the entire file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# Return to the top of the file.
rewind(current_file)

print "Let's print three lines:"
# Lines 35 - 40 asking the file to print the first 3 lines only.
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
