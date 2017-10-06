class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayinfo(self):
		print self.price
		print self.max_speed
		print self.miles
		# return self.miles
	def ride(self):
		print "Riding: {}".format(self.miles)
		self.miles += 10
		# return self
	def reverse(self):
		print "Reversing"
		if self.miles >= 5:
			self.miles -=5
		# return self
bike = Bike(50, 75)
bike.ride()
bike.ride()
bike.ride()
bike.reverse()
bike.displayinfo()