#input

#output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"


l = ['magical unicorns', 19, 'hello', 98.98, 'world']
def identify_list_type(lst):
    new_string = ""
    total = 0

    for value in lst:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_string += value

    if new_string and total:
        print "The array you entered is of mixed type"
        print "String:", new_string
        print "Total:", total

    elif new_string:
        print "The array you entered is of string type"
        print "String:",new_string

    else:
        print "The array you entered is of number(float or int) type"
        print "Total:", total

print identify_list_type(l)
