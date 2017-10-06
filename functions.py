# #function with two parameters(inputs to the function)
# def add(a,b):
# 	x = a + b
# 	return x 
# print(3,5) # < ---- invoking/calling our function, followed by "()"...prints 8

# def say_hi(name):
# 	print "Hi, " + name
# #invoking the function
# say_hi("Michael")
# say_hi("Anna")

##########

#debugging section
def multiply(arr, num):
	for x in range(len(arr)):
		arr[x] *= num
	return arr

a = [2, 4, 10, 16]
b = multiply(a,5)
print b 