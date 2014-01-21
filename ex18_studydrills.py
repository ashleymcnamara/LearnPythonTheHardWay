# Study Drills

# Write out a function checklist for later exercises. Write these on an index card and keep it by you while you complete the rest of these exercises or until you feel you do not need it:

# Did you start your function definition with def? > YES
# Does your function name have only characters and _ (underscore) characters? > YES
# Did you put an open parenthesis ( right after the function name? > YES
# Did you put your arguments after the parenthesis ( separated by commas? > YES
# Did you make each argument unique (meaning no duplicated names)? > YES
# Did you put a close parenthesis and a colon ): after the arguments? > YES
# Did you indent all lines of code you want in the function four spaces? No more, no less. > YES
# Did you "end" your function by going back to writing with no indent (dedenting we call it)? > YES
# And when you run ("use" or "call") a function, check these things:
#
# Did you call/use/run this function by typing its name? > YES
# Did you put the ( character after the name to run it? > NO
# Did you put the values you want into the parenthesis separated by commas? > YES
# Did you end the function call with a ) character? > YES
# Use these two checklists on the remaining lessons until you do not need them anymore.

# Finally, repeat this a few times:
# "To 'run,' 'call,' or 'use' a function all mean the same thing."
#------------------------------------------------------------------------------------

# Print these two arguments
def print_two(*args):
# The arguments are listed and seperated by a comma
		arg1, arg2 = args
# Print and define arguments 1 and 2
		print "arg1: %r. arg2: %r" % (arg1, arg2)
# Reprint.
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
# Just print the first one
def print_one(arg1):
	print "arg1: %r" % arg1
# Print zero arguments
def print_none():
	print "I got nothin'."
# Defining values
print_two("Ashley","McNamara")
print_two_again("Ashley","McNamara")
print_one("First!")
print_none()
