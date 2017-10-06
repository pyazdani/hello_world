# track products.  Creating a product class

# ATTRIBUTES: Price, Item Name, Weight, Brand, Cost, Status: default "for sale"

# METHODS: 
		#   Sell: changes status to "sold"
		# 	Add Tax: Takes decimal amount tax and returns price of the item including sales tax
		# 	Return: Takes reason for product being returned and changes status accordingly. 
		# 		If item is defective, change status to "defective" and price to 0
		# 		If item is returned in the box, keep status as "for sale"
		# 		If item has been opened, set status to "used" and apply a 20% discount to price
		# 	Display Info: 
		# 		Show all the products details
		# every METHOD that doesnt have to return something should return self so methods can be chained

class Product(object):
	def __init__(self, price, item_name, weight, brand, cost, status, tax):
		self.price = price 
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = status
		self.tax = float(tax)
		# self.displayInfo()	

	def Sell(self):
		self.status = "sold"
		return self 
	
	def addTax(self):
		self.price = self.price + (self.price * float(self.tax))
		return self

	def Return(self):
		if self.status == "defective":
			self.status = "defective"
		elif self.status == "opened":
			self.status = "used"
			self.price = self.price - (self.price * .20)
		elif self.status == "returned in the box":
			pass 
		return self
	def displayInfo(self):
		print "Price: "+str(self.price)
		print "Item: "+self.item_name
		print "Weight: "+str(self.weight)
		print "Brand: "+self.brand
		print "Cost: "+str(self.cost)
		print "Status: "+self.status

product1 = Product(50, "Basketball Shoes", 20, "Nike", 25, "for sale", .12)
product2 = Product(73, "Football Cleats", 10, "Adidas", 20, "opened", .14)

product1.addTax().displayInfo()
product2.addTax().Return().displayInfo()