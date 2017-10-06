# generates ten scores between 60 and 100.  Each time a score is generated, displays grade
# and score
#Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

def scores_and_grades():
	for i in range(1, 11):
		import random
		score = random.randint(60,100)
		if score >= 60 and <= 69:
			print "Score:", score, "; Your grade is D"
		elif score >= 70 and <= 79:
			print "Score:", score, "; Your grade is C" 
		elif score >= 80 and <= 89:
			print "Score:", score, "; Your grade is B"
		# elif score >= 70 and <=79:
		# 	print "Score:", score, "; Your grade is C" 
		else:
			print "Score:", score, "; Your grade is A" 
scores_and_grades()