people = 130
cars = 140
buses = 315


if cars > people:
	print "We shoud take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

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

if cars < people and busses > cars:
	print "What am I doing?"
else:
	print "I have no idea"
