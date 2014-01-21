# Study Drills

# Memorize all the escape sequences by putting them on flash cards.
# Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?
# Combine escape sequences and format strings to create a more complex format.
# Remember the %r format? Combine %r with double-quote and single-quote escapes and print 
# them out. Compare %r with %s. Notice how %r 
# prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?
# -------------------------------------------------------------------------------

# Original code

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat 
#------------------------------------------------------------------------------

# Escape Sequences

# \\	Backslash ()
# \'	Single-quote (')
# \"	Double-quote (")
# \a	ASCII bell (BEL)
# \b	ASCII backspace (BS)
# \f	ASCII formfeed (FF)
# \n	ASCII linefeed (LF)
# \N{name}	Character named name in the Unicode database (Unicode only)
# \r ASCII	Carriage Return (CR)
# \t ASCII	Horizontal Tab (TAB)
# \uxxxx	Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v	ASCII vertical tab (VT)
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh

# -------------------------------------------------------------------------------
# Homework Code

# Line 44 we used the "\t" to tab the text.
tabby_cat = "\tI'm tabbed in."
# Line 46 we used "\n" to split the line.
persian_cat = "I'm split\non a line."
# Line 48 we used "\\" to insert 1 backslash into the sentence. 
backslash_cat = "I'm \\ a \\ cat."
# In lines 46 & 51 I changed from single ''' to double """ and the only difference is that
# it's cleaner looking code.
# In lines 50 - 52 the "/t" is used to tab the test and add a bullet point of "*"
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
# Lines 62 - 65 are printing the text assigned to each variable.
print "I am going to add some esacpe sequences to this part of my code"
# Using the \\ on ether side of a print statement inserts forward slashes
print "For instance if I wanted to put a backslash in this sentence I would - \\" 
print "But what if I wanted to add backslash_cat to this part? I would use (percent sign) and the letter s, like this - %s " % backslash_cat
# Line 72 print statement is completed using the %r (carriage return) sequence to complete the rest of the sentence.
print "tabby cats say: %r" % tabby_cat 
# In line 74, when using %s vs %r you see that tabby cat is printed using words whereas the %r just reads the line as is.
print "How does it read when I use the percent sign and the letter s to print tabby cat? Lets do it right here - %s" % tabby_cat
# Line 76 I use the \" sequence to quote a portoin of my print statement
print "What if I wanted to add quotes to this bit of code? I would use the backslash and quote on either side of my quote \"and quote this\"."
# Line 78 I use the \n sequence to print the rest of the code on another line.
print "What if I like to write really long print statements and I wanted to use more than one line? I would use forward slash and the letter n \nso the code doesn't trail on and on and on and on...?"
print persian_cat
print backslash_cat
print fat_cat 
