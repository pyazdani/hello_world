# students = [
# 	{'first_name' : 'Michael', 'last_name' : 'Jordan'},
# 	{'first_name' : 'John', 'last_name' : 'Rosales'},
# 	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
# 	{'first_name' : 'KB', 'last_name' : 'Tonel'},
# 	]

# for student in students:
# 	print student["first_name"], student["last_name"]

# PART 2

users = {
	'Students':[
	{'first_name' : 'Michael', 'last_name' : 'Jordan'},
	{'first_name' : 'John', 'last_name' : 'Rosales'},
	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
	{'first_name' : 'KB', 'last_name' : 'Tonel'},
	],

	'Instructors':[
	{'first_name' : 'Michael', 'last_name' : 'Choi'},
	{"first_name" : "Martin", "last_name" : "Puryear"}
	]
}

# ** bonus code...would print out 'Michael' **
# print user["Students"][0]["first_name"]

for user in users:
	print user
	sum = 1
	for x in users[user]:
		print "{} - ".format(sum), x["first_name"], x["last_name"], " - ", len(x["first_name"])+len(x["last_name"])
		# either top or bottom line works the sum
		# print str(sum)+" - ", x["first_name"], x["last_name"]
		sum += 1
