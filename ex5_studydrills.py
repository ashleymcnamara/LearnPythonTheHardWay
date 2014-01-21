# Study Drills

# Change all the variables so there isn't the my_ in front. Make sure you change the name everywhere, not just where you used = to set them.
# Try more format characters. %r is a very useful one. It's like saying "print this no matter what."
# Search online for all of the Python format characters.
# Try to write some variables that convert the inches and pounds to centimeters and kilos. Do not just type in the measurements. Work out the math in Python.

name = 'Ashley N. McNamara'
age = 32 
height = 55 
weight = 120 
eyes = 'blue'
teeth = 'white'
hair = 'blonde'

print "Let's talk about %s." % name #Used different format characters 
print "She's %r inches tall." % height
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the soda." % teeth

print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)

# Writing my own that converts pounds into kilos 
my_weight = 120
kilos = 0.453592

print "I am %d lbs" % my_weight
print "That is %d in kilos" % (my_weight * kilos)
