# Study Drills

# Try giving fewer than three arguments to your script. See that error you get? 
# See if you can explain it.
# Write a script that has fewer arguments and one that has more. 
# Make sure you give the unpacked variables good names.
# Combine raw_input with argv to make a script that gets more input from a user.
# Remember that modules give you features. Modules. Modules. 
# Remember this because we'll need it later.

#------------------------------------------------------------------------------
from sys import argv 
# When I remove an argument in the script I see the following error message:
#
#  File "ex14.py", line 15, in <module>
#    script, First, Second, Third = argv
# ValueError: need more than 3 values to unpack
 script, First, Second, Third = argv
#
# I believe that this message simply means that in order to run the script there must 
# be at least 3 values

print "what is the script called?", raw_input(script) 
print "What is your first variable?", raw_input(First)
print "What is your second variable?", raw_input(Second)
print "What is your third variable?", raw_input(Third)

#------------------------------------------------------------------------------------------

# Below I will write a script that has fewer arguments

from sys import argv

script, ashley, mcnamara = argv

print "What is the name of the script?", raw_input(script)
print "What is your first name?", raw_input(ashley)
print "What is your last name?", raw_input(mcnamara)

# When I ran the script with fewer arguments it worked just fine.

#-------------------------------------------------------------------------------------------

# In lines 45 - 57 I combined raw_input with argv to get more input from the user.
from sys import argv

script, ashley, mcnamara = argv

print "What is the name of the script?\n", raw_input(script)
print "Do you agree with the statement?"
print  raw_input("> ")
print "What is your first name?\n", raw_input(ashley)
print "Do you agree with the statement?"
print raw_input("> ")
print "What is your last name?\n", raw_input(mcnamara)
print "Do you agree with this statement?"
print raw_input("> ")
