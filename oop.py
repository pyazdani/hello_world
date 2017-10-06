class Student(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.numberOfBelts = 0
    def addBelt(self):
        self.numberOfBelts += 1
        return self
    def say(self, thing):
        print self.name, "says", thing
        return self

class Person(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def say(self, thing):
        print self.name, "says", thing

class Student(Person):
    def __init__(self, name, email):
        super(Student, self).__init__(name, email)
        self.numberOfBelts = 0
    def addBelt(self):
        self.numberOfBelts += 1
        return self
    def show(self):
        print self.name, "has", self.numberOfBelts, "belt(s)"
        return self
    # def say(self, thing):
    # 	super(Student, self).say(thing)
    # 	print "something else"

# bob = Person("Bob", "bob@gmail.com")
# bob.say("hello")

# jenny = Student("Jenny", "jenny@gmail.com")
# jenny.say("goodbye")



# amina = Student("Amina", "amina@google.com")
# amina.addBelt()
# print amina.name, amina.email, amina.numberOfBelts

class MyNumber(int):
	def sayHello(self):
		print self, "say hello"

a = MyNumber(3)
# a.sayHello()
b = 2
# b.sayHello()
print a + b