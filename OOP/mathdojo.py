# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.
# Then create a new instance called md. It should be able to do the following task:
# md.add(2).add(2,5).subtract(3,2).result
# which should perform 0+2+(2+5)-(3+2) and return 4.

class MathDojo(object):
	def __init__(self, arg1, *args):
		self.arg1 = 0

	def add(self):
		self.arg1 += *args

	def subtract(self):
		self.arg1 -= *args

	def result(self):
		print self.arg1

test1 = MathDojo(0)
test1.add(2).add(2,5).subtract(3,2).result

