class rap(object):

	def __init__ (self, lyrics):
		self.lyrics = lyrics

	def old_school_rap(self):
		for line in self.lyrics:
			print line

vanilla_ice = rap(["All right stop, Collaborate and listen",
                   "Ice is back with my brand new invention"])

digital_underground = rap(["All right! Stop whatcha doin",
                           "cause I'm about to ruin the image and the style"])

biggie_smalls = rap(["To all the ladies in the place with style and grace",
                     "Allow me to lace these lyrical duches in your bushes",
                     "Who rock grooves and make moves with all the mommies"])

vanilla_ice.old_school_rap()

digital_underground.old_school_rap()

biggie_smalls.old_school_rap()
