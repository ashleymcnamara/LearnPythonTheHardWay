## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
	pass

# Dog is-a animal
class Dog(Animal):

	def __init__(self, name):
		# dog has-a name
		self.name = name

# a cat is-a animal
class Cat(Animal):

	def __init__(self, name):
		# cat has-a name
		self.name = name

# Person is-a object
class Person(object):

	def __init__(self, name):
		# person has-a name
		self.name = name

		# Person has-a pet of some kind
		self.pet = None

# Employee is-a person
class Employee(Person):
	# Self has-a name and a salary
	def __init__(self, name, salary):
		# Call __init__ method of employees super-class (person)
		super(Employee, self).__init__(name)
		# Employee has-a salary
		self.salary = salary


# Fish is-a object
class Fish(object):
	pass

# Salmon is-a fish
class Salmon(Fish):
	pass

# Halibut is-a fish
class Halibut(Fish):
	pass


# Rover is-a dog
rover = Dog('Rover')
print "Rover is a dog"
print "Dogs don't like waterslides."
print "\n"
# satan is-a cat
satan = Cat('Satan')
print "Cat's are evil and they also hate waterslides."
print "\n"
# Mary is-a person
mary = Person('Mary')
print "Mary likes cats."
print "....puuurrrrrrrr...."
# Mary has-a pet cat named satan
mary.pet = satan
print "but Mary is a unstable."
print "\n"
# Frank is an employee
frank = Employee("Frank", 12000)
print "Frank makes 12k, which isn't even min wage but"

# frank has-a pet dog named rover
frank.pet = rover
print "to make up for the fact that Frank is broke and alone,"
print "Frank has a dog named Rover and Rover is a dumb ass."
# Flipper is-a fish
flipper = Fish()
print "\n"
# Crouse is-a Salmon
crouse = Salmon()

# Harry is-a Halibut
harry = Halibut
print "\n"
print "Mary is a crazy cat lady, she has %s and their names are..." % "9 cats"
mary.cat = ('Oscar', 'Tom', 'Jerry', 'Crazy', 'Loco', 'Fleas', 'George', 'Butter', 'Psycho')
print mary.cat
print "\n"
print "Mary likes to sing to her cats, you know.. because she's crazy."
print "\n"
print "Her favorite song is:"
mary.song = ("Kitty cat kitty cat, \nWhere you at pretty kitty cat, \nSee me out pretty cat, \nPretty kitty kitty cat, \nKitty cat, Where you at pretty kitty cat, \nYou are a bad pretty cat, \nPretty kitty kitty cat, \nKitty cat kitty cat, \nWhere you at pretty kitty cat, \nSee me out pretty cat, \nPretty kitty kitty cat, \nKitty cat, \nWhere you at pretty kitty cat, \nYou are a bad pretty pretty pretty kitty")
print mary.song
