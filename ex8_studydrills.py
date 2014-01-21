# Study Drills

# Do your checks of your work, write down your mistakes,
# and try not to make them on the next exercise.
# Notice that the last line of output uses both single-quotes 
# and double-quotes for individual pieces. Why do you think that is?
# -------------------------------------------------------------------------------
# There is no difference between single '' and double " " it's a personal preference.
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"but it didn't sing.",
	"So I said goodnight."
	)
