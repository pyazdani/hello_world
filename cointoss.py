# # simulates the tossing of a coin 5000 times

def coinToss():
	import random
	heads = 0
	tails = 0
	result = 0
	for i in range(1, 5001):
		result = random.randint(0,1)
		if result == 1:
			heads += 1
			print "Throwing a coin...It's heads!...Got", heads, "head(s) so far and", tails, "tail(s) so far"
		else:
			tails += 1
			print "Throwing a coin...It's tails!...Got", heads, "head(s) so far and", tails, "tail(s) so far"
coinToss()

