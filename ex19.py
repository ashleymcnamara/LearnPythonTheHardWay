def cheese_and_crackers(cheese_count, boxes_of_crackers, stinky):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of boxes of crackers!" % boxes_of_crackers
	print "you have %d pieces of stinky cheese" % stinky
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
stinky = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers, stinky) 


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6, 8 + 4)


print "And we can combine the two, cariables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000, stinky + 30)
