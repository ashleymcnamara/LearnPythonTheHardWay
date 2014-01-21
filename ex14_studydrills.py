# Study Drills

# Find out what Zork and Adventure were. Try to find a copy and play it.
# Change the prompt variable to something else entirely.
# Add another argument and use it in your script.
# Make sure you understand how I combined a """ style multiline string with 
# the % format activator as the last print.
#
#-------------------------------------------------------------------------
#Zork and Adventure is a question and answer game. 
#
from sys import argv

script, one_more, user_name = argv
# The prompt variable is being used to place whatever is in the '' at the start 
# of user input (raw_input) areas. So when I changed from '> ' to '## ' it will
# show ## instead of >
prompt = '## '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "This is the section where I add another argument."
print "I added the one_more argument. Can you see one more? ---> %s " % one_more
one_more = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)
# Using the % at the end of this print statement assigns user input to each %r in your 
# print statement.
print """
Alright, so you said %r about liking me.
and you said %r that you see the added argument.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, one_more, lives, computer)

#------------------------------------------------------------------------------
# Triple quotes strings multiple lines of test together and prints them as one. 
# Below is an example:
print"""
So I have this paragraph
and in this paragraph I don't want to use
print at the beginning of each line
so instead of using print at the beginning of each line
I just use triple quotes"""
