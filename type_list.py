#input
l = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"

# # input
# l = [2,3,1,7,4,12]
# #output
# "The list you entered is of integer type"
# "Sum: 29"

# # input
# l = ['magical','unicorns']
# #output
# "The list you entered is of string type"
# "String: magical unicorns"

strng = ""
total = 0

for val in l:
	if type(val) == int:
		total = total + val
	elif type(val) == str:
		strng = strng + val

if strng and total:
	print "The list you entered is of mixed type"
	print "String:", strng
	print "Sum: {}".format(total)

elif total:
	print "The list you entered is of integer type"
	print "Sum:", total

elif strng:
	print "The list you entered is of string type"
	print "String:", strng
