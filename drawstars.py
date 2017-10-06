# takes a list and prints out * depending on values in that list

x = [4, 6, 1, 3, 5, 7, 25]
def drawStars(arr):	
	for val in arr:
		print "*" * val
drawStars(x)
