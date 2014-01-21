print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheesecake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. You punch the bear in the nose and run like hell"

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. GOOD JOB!"
	elif bear == "2":
		print "The bear eats your legs off. GOOD JOB!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
		print "And if doing %s is better then you live" % bear

elif door == "2":
		print "You stare into the endless abyss at Cthulhu's retina."
		print "1. Blueberries."
		print "2. Yellow jacket clothepins."
		print "3. Understanding revolvers yelling melodies."
		print "4. run around in a circle until the bear gets tired."

		insanity = raw_input("> ")

		if insanity == "1" or insanity == "2":
			print "Your body survives powered by a mind of jello. GOOD JOB!"
		else:
			print "The insanity rots your eyes into a pool of muck. GOOD JOB!"
			print "insanity is insane"

		bear = raw_input("> ")

elif bear == "2" and bear > "3":
	print "1. bears are cool"
	print "2. bears are evil"
	print "3. bears are kooks"
	print "You stumble around and fall on a knife and die. GOOD JOB!"
else:
	print "Testing some code out"
