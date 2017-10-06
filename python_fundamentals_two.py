# print all the odd numbers from 1 - 1000

for count in range(1, 1000):
  if count%2 != 0:
  	print count

# print all the multipleds of 5 from 5 - 1,000,000

for count in range(5, 1000000):
	if count%5 == 0:
		print count

# prints the sum of all the values in the list

a = [1, 2, 5, 10, 255, 3]
print sum(a)

# prints the average of the values in the list

a = [1, 2, 5, 10, 255, 3]
print sum(a)/(len(a))
