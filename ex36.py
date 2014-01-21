from sys import exit 

def joe():

	print "Joe has a beautiful woman in his sights, but she is diseased!"
	print "which disease does she have? herpes, aids, or the clap?"
	
	next = raw_input()

	if next == "herpes":
		std_treatment()
	elif next == "aids":
		dead("Joe is DEAD!")
	if next == "clap":
		std_treatment()
	else:
		dead("Joe is DEAD!")

def welcome_back():
	print "Joe has overcome his disease but can he do it again? Don't underestimate how dumb Joe really is."
	print "Joe hires a hooker but she is also diseased, what disease does the hooker have??"
	print "aids, warts, or plague"

	next = raw_input()

	if next == "aids":
		dead("Joe contracts AIDS and dies a slow, painful, death.")
	elif next == "warts":
		std_treatment()
	if next == "plague":
		dead("Joe contracts the plague and dies.")
	else:
		std_treatment()

def std_treatment():
	print "Joe has contracted a non-life threatening disease. How is his disease treated?"
	print "Pills, Creams, Or Dick Scraping??"

	next = raw_input()

	if next == "creams":
		std_clinic()
	elif next == "pills":
		std_clinic()
	if next == "dick scraping":
		std_clinic()
	else:
		dead("Joe goes untreated and dies a painful death.")

def std_clinic():
	print "Joe is being treated for his STD. How long will he be out of commission?"
	print "a week, a month, or a year?"

	next = raw_input()

	if "a week" in next:
		week_treatment()
	elif "a month" in next:
		month_treatment()
	elif "a year" in next:
		year_treatment()
	else:
		dead("Joe decided to go right back to being a whore and dies from infection.")

def month_treatment():
	print "Joe is out of commission for a month and is already making plans to get back to fucking."
	print "Joe considers using condoms to prevent further spreading but isn't sure he cares."
	print "Doe he decide to use the condoms? Yes or No?"

	next = raw_input()

	if "yes" in next:
		safety_zone()
	elif "no" in next:
		danger_zone()
	else:
		dead("Joe dies from indecision, his brain is just too small.")

def week_treatment():
	print "Joe is out of commission for a week but can't stiffle that sex-aholic feeling so he masterbates furiously!"
	print "How many times a day does Joe masterbate?"

	next = raw_input()

	if next > 100:
		safety_zone()
	elif next < 50:
		dead("Joe masterbates himself to death.")
	else:
		danger_zone()

def year_treatment():
	print "Joe is out of commission for an entire year and the thought of having to masterbate for that long makes him furious!"
	print "Does Joe continue to masterbate in order to stop the spread of infection?"
	print "Yes or No"

	next = raw_input()

	if next == "yes":
		safety_zone()
	elif next == "no":
		danger_zone()
	else:
		dead("Joe is proving he isn't capeable of making decisions and dies.")

def danger_zone():
	print "Even though the Dr's at the clinic suggested that he take a fuck break, Joe thinks he knows better."
	print "How many others will Joe infect?"
	
	next = raw_input()

	if next > 100:
		safety_zone()
	elif next < 50:
		dead("Joe causes an STD outbreak that spreads world wide. Killing millions, including himself")
	else:
		start()

def safety_zone():
	print "Joe is making some rare wise decisions and his infection is clearing up!"
	print "Does Joe wait to fully heal? Yes or No?"
	
	next = raw_input()

	if next == "yes":
		welcome_back()
	elif next == "no":
		dead("Joe refuses to wait until he is fully healed and dies from infection.")
	else:
		dead("Joe dies from indecision.")

def dead(why):
	print why, "Because Joe is an idiot."
	exit(0)

def start():
	print "Joe has an STD, It's either life treatening or not"
	print "Which one is it, life of death?"

	next = raw_input()

	if next == "life":
		joe()
	elif next == "death":
		dead("Joe contracted a deadly disease.")
	else:
		joe("Joe is confused about his condition.")

start()

