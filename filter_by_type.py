sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

# if integer is greater than or equal to 100, print "That's a big number" if less than 100, print that's a small number
if type(spI) == int:
	if spI > 100:
		print "That's a big number!"
	else:
		print "That's a small number"

# if string is great >= 50 characters, print "Long Sentence.".  If under, "Short sentence."
if type(sS) == str:
	if len(sS) >= 50:
		print "Long Sentence"
	else:
		print "Short Sentence"

# if length of list is >= 10, print "Big List".  If < 10, print "Short List"
count = 0
for val in spL:
	count = count + 1
if count >= 10:
	print "Big List"
else:
	print "Short List"


