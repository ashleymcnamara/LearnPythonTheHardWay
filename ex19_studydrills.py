#Study Drills

# Go back through the script and type a comment above each line explaining in English what it does.
# Start at the bottom and read each line backward, saying all the important characters.
# Write at least one more function of your own design, and run it 10 different ways.
#-----------------------------------------------------------------------------------------------
# Line 8 is defining cheese and crackers as 3 variables.
def cheese_and_crackers(cheese_count, boxes_of_crackers, stinky):
# Line 10 is saying insert the number of cheeses here %d
	print "You have %d cheeses!" % cheese_count
# Line 12 is putting the value of boxes of crackers in the print statement
	print "You have %d boxes of boxes of crackers!" % boxes_of_crackers
# Line 14 is doing the same as line 12
	print "you have %d pieces of stinky cheese" % stinky
	print "Man that's enough for a party!"
# Line 17 is printing a statement but it's also using \n to make a new line.
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# Assigns the following values to cheese and crackers.
cheese_and_crackers(20, 30, 30)

print "OR, we can use variables from our script:"
# Line 26-28 are also taking those variables and assigning values.
amount_of_cheese = 10
amount_of_crackers = 50
stinky = 30
# cheese and crackers = the following variables.
cheese_and_crackers(amount_of_cheese, amount_of_crackers, stinky) 

# Line 35 takes cheese and crackers and assigns values then breaks it down
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6, 8 + 4)


print "And we can combine the two, variables and math:"
# Line 39 takes the values and adds onto it
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000, stinky + 30)
