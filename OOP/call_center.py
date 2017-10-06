#create a call center with two classes

# ATTRIBUTES:
# Unique Id
# Caller Name
# Phone NUmber
# Time of Call
# Reason

# METHODS
# add: adds a new call to the end of the call list
# remove: removes a call to the end of the call list
# info: prints the name and phone number for EACH CALL(for loop) on the queue list

from datetime import datetime # <----Library file.  Says "From datetime import datetime"

class Call(object):
	def __init__(self,name,phoneNumber, reason):
		self.id = id(self) # <---"id" is a built in function in python.  "id(self)" generates a random id
		self.name = name
		self.phoneNumber = phoneNumber
		self.timeOfCall = datetime.now() #<----Calling/referring to datetime function from datetime library
		self.reason = reason
		# self.display()

	def display(self):
		print self.id, self.name, self.phoneNumber, self.timeOfCall, self.reason

callWill = Call("Will", 703-999-5289, "Boredom")
# callWill.display()

class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queueSize = 0

	def add(self, name, phoneNumber, reason):
		self.calls.append(Call(name, phoneNumber, reason))
		self.queueSize += 1
		return self

	def remove(self):
		self.calls.remove(self.calls[0])
		self.queueSize -= 1
		return self

	def info(self):
		for call in self.calls:
			call.display()
			# print type(call)

		print "Current Queue: "+str(self.queueSize)+" callers."
		# print type(self) <--- try this to see what it prints

center = CallCenter()
center.add("Will", 1234567, "Just Because")
center.add("Motuma", 765421, "Has a Question")
center.add("Olu", 321455, "Customer Service")
center.add("Tri", 1234321, "Customer Complaint")


center.info()
# center.remove() # <--- calls on the remove function to remove a call from the center list
center.info()


# center = CallCenter90
# center.add().add().add()

