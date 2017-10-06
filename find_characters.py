#takes a list of strings and a single character, prints a new list of all the strings containing that character
word_list = ["hello", "world", "my", "name", "is", "Anna"]
char = "o"
new_list = ""
for i in word_list:
	if word_list[i].find(char) != -1:
		new_list.append(word_list[i])
print new_list