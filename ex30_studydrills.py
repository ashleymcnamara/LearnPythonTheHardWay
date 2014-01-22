# Study Drills

# Try to guess what elif and else are doing.
# Change the numbers of cars, people, and buses and then trace through each if-statement
# to see what will be printed.
# Try some more complex boolean expressions like cars > people and buses < cars.
# Above each line write an English description of what the line does.
#---------------------------------------------------------------------------------------
#
people = 130
cars = 140
buses = 315
# I believe it goes like this, If this statement is true then print this if it's false go to elif
# if elif is also false then print the else statement.
#
# Line 17, if there are more cars than people, print "We should take the cars."
if cars > people:
	print "We shoud take the cars."
# Line 20, if there are more people than cars, print "We should not take the cars."
elif cars < people:
	print "We should not take the cars."
# Line 23, if neither of the above are true then print "We can't decide."
else:
	print "We can't decide."
# Lines 26 - 36 are doing the same.
if buses > cars:
	print "That's too many busses."
elif buses < cars:
	print "Maybe we could take the busses"
else:
	print "We still can't decide."

if people > buses:
	print "Alright, lets just take the busses"
else:
	print "Fine, lets stay home then."
# Line 39, If there or more people than cars and more busses than cars then print "What am I doing?"
# If false then print "I have no idea."
if cars < people and busses > cars:
	print "What am I doing?"
else:
	print "I have no idea"
