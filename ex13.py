from sys import argv 

script, First, Second, Third = argv

print "what is the script called?", raw_input(script) %r
print "What is your first variable?", raw_input(First)
print "What is your second variable?", raw_input(Second)
print "What is your third variable?", raw_input(Third)
