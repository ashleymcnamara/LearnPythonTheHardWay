# Study Drills

# In this Study Drill, try to guess what you think the if-statement is and what it does. 
# Try to answer these questions in your own words before moving on to the next exercise:

# What do you think the if does to the code under it?
# Why does the code under the if need to be indented four spaces?
# What happens if it isn't indented?
# Can you put other boolean expressions from Exercise 27 in the if-statement? Try it.
# What happens if you change the initial variables for people, cats, and dogs?
#--------------------------------------------------------------------------------------

people = 20
joes = 30
dogs = 15
true = 1
false = 0
# Line 20, is saying, only print the statements that are true
#
if true < false:
	print "Does true = false?"
# Line 24, are there more Joe's that people? The answer is true because there are 
# 30 Joes and 20 People
if people < joes:
	print "Too many joes! The world is doomed!"
# Line 28, are there more people than joe's? The answer is False. 
# There are 30 Joe's and 20 People
if people > joes:
	print "Not many joes! The world is saved!"
# Line 32, are there more dogs than people? The answer is False. 
# There are 20 people and 15 dogs. 
if people < dogs:
	print "The world is drooled on!"
# Line 36, are there more people than dogs? The answer is True.
# There are 20 people and 15 dogs. 
if people > dogs:
	print "The world is dry!"

# Line 40, dogs plus 2
dogs += 2
# Line 42, is true because there are more people than dogs.
if people >= dogs:
	print "People are greater than or equal to dogs."
# Line 45, is false because there are more people than dogs.
if people <= dogs:
	print "People are less than or equal to dogs."
# Line 48, the answer is false because people and dogs are not equal.
if people == dogs:
	print "People are dogs"
