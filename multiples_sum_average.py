# print all odds from 1 to 1000.
for i in range(0, 1001):
	if i % 2 != 0:
		print i 

# multiples of 5 from 5 to 1000000.
for i in range(5, 1000001):
	if i % 5 == 0:
		print i

# prints the sum of all the numbers in an list.
a = [1, 2, 5, 10, 255, 3]
sum = 0
for val in a:
	sum += val
print sum

# prints average of the values in a list.
a = [1, 2, 5, 10, 255, 3]
counter = 0
sum = 0
average = 0
for val in a:
	sum += val
	counter = counter + 1

average = sum / counter
print average




