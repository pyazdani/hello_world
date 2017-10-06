# # counts 1 to 2000, prints numbers and whether it's odd or even
# def odd_even():
# 	for i in range(1, 201):
# 		if i % 2 == 0:
# 			print "Number is", i, "This is an even number"
# 		else:
# 			print "Number is", i, "This is an odd number"
# odd_even()

# # takes in two arguments, multiplies list by second argument
# def multiply(arr, num):
# 	for x in range(len(a)):
# 		a[x] *= num
# 	return arr
# a = [2, 4, 10, 16]
# b = multiply(a, 5)
# print b


# # function that takes the multiply function call as an arguement.  
def layered_multiples(arr):
	arr = [[2,4,5]
	b = multiply(a, 5)
	for indie in arr:
		for number in indie:
			arr[number] *= 3
	return arr
x = layered_multiples(multiply([2,4,5],3))
print x

