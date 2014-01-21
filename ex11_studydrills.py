# Study Drills

# Go online and find out what Python's raw_input does.
# Can you find other ways to use it? Try some of the samples you find.
# Write another "form" like this to ask some other questions.
# Related to escape sequences, try to find out why the last line has '6\'2"' with that \'sequence.
# See how the single-quote needs to be escaped because otherwise it would end the string?
# -----------------------------------------------------------------------------------------------

# raw_input is a prompt that lets a user answer a question or interact with the code.
age = raw_input("How old are you? ") 
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")
# Line 28 takes the variables above and inserts the raw_input values into the print statement.
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

#----------------------------------------------------------------------------------------------

# I created the code in lines 22 - 26
# I defined my variables and use the raw_input prompt to ask the user a question 
bunny = raw_input("How adorable is the bunny?")
squeeze = raw_input("Do you want to squeeze the bunny?")
scale = raw_input("On a scale of 1 - 10 how cute is the bunny?")
# Line 37 I use the \n to put my print statement on more than one line and I used the %r to input the answers given to the raw_input prompt. 
print "Apparently you think the bunny is %r . \nWhen asked if you wanted to squeeze the bunny you said %r . \nOn a scale of 1-10 you think the bunny is a %r" % (bunny, squeeze, scale)
