string = ""
sum = 0


for i in x:
    if isinstance(i, int):
        sum += i
    elif isinstance(i, str):
        string = string  + " " + i

typeof = ""

if all(type(item) is int for item in x):
    typeof = "integer"
elif all(type(item) is str for item in x):
    typeof = "string"
else: typeof = "mixed"
print "The array you entered is of", typeof, "type."
if sum > 0:
    print "Sum:", sum
if string:
    print "String:", string
