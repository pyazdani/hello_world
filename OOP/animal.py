# # Animal class with two child classes, Dog and Dragon

# # Animal Class:
# 	ATTRIBUTES: 
# 		name
# 		health
# 	METHODS:
# 		walk: decreases health by one
# 		run: health decreses by five
# 		display health: print to the terminal the animal's health

# 	INSTANCE:
# 		animal1 - walk() 3 times, run() twice, displayHealth() to confirm that the health has changed

class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def Walk(self):
		self.health -= 1
		return self

	def Run(self):
		self.health -= 5
		return self

	def DisplayHealth(self):
		print "Name: " +self.name
		print "Health: "+str(self.health)

animal1 = Animal("Felix")
animal1.Walk().Walk().Walk().Run().Run().DisplayHealth()

# # Dog Class:
# 	ATTRIBUTES:
# 		Default health of 150
# 	METHODS:
# 		Pet: increases health by 5

# 	INSTANCE: 
# 		Have the dog walk() 3 times, run() twice, pet() once, and have it displayHealth()

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__()
        self.health = 150

    def Pet(self):
    	self.health += 5

dog1 = Dog("Snoop")
dog1.Walk().Walk().Walk().Run().Run().Pet().DisplayHealth()

# # Dragon Class:
# 	ATTRIBUTES:
# 		Deatult health of 170
# 	METHODS:
# 		Fly: Decreases health by 10
# 		dispalyHealth prints health by calling the parent method and prints "I am a Dragon"

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__()
		self.health = 170

	def Fly(self):
		self.health -= 10

	def displayHealth(self):
		super(Dragon, self).__init__()
		print "I am a Dragon"

dragon1 = Dragon.DisplayHealth()


