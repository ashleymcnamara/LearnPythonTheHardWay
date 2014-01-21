# Study Drills

# In Terminal where you normally run python to run your scripts, type pydoc raw_input. 
# Read what it says. If you're on Windows try python -m pydoc raw_input instead.
# Get out of pydoc by typing q to quit.
# Look online for what the pydoc command does.
# Use pydoc to also read about open, file, os, and sys. 
# It's alright if you do not understand those; just read through and take notes 
# about interesting things.
# -----------------------------------------------------------------------------------------------

# raw_input is a prompt that lets a user answer a question or interact with the code.
age = raw_input("How old are you? ") 
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")
# Line 28 takes the variables above and inserts the raw_input values into the print statement.
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

#----------------------------------------------------------------------------------------------

# If I run pydoc raw_input, the following information pops up on the screen.

# Help on built-in function raw_input in module __builtin__:

# raw_input(...)
#    raw_input([prompt]) -> string
    
#    Read a string from standard input.  The trailing newline is stripped.
#    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
#    On Unix, GNU readline is used if enabled.  The prompt string, if given,
#    is printed without a trailing newline before reading.
#(END) 

# This would lead me to assume that "pydoc" is python documentation. Groovy. 
