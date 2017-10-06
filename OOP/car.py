# creates a class called Car.  User specifies(__init__) ATTRIBUTES: price, speed, fuel, mileage.
# If price > 10000, set the tax to be 15%.  Otherwise, 12%

#Create six different instance of Car class.  
#In the class, have a method called display_all() that returns all the info as as string
#In you __init__(), call on this display_all() method to display information about the car 
#	once the ATTRIBUTES have been defined.

#sample output:
# Price: 2000
# Speed: 35mph
# Fuel: Full
# Mileage: 15mpg
# Tax: 0.12

class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel  = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = "15%"
		else:
			self.tax = "12%"
		self.display_all()

	def display_all(self):
		print "Price: "+str(self.price)
		print "Speed: "+str(self.speed)+"mph"
		print "Fuel: "+str(self.fuel)
		print "Mileage: "+str(self.mileage)+"mpg"
		print "Tax: "+str(self.tax)
car1 = Car(12000, 50, "Full", 20)	
# car1.display_all() < ---No need to call this function, as it already runs within the __init__ function
