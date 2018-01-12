#Question 1:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

#Notes:
#-input of this program is a range (a start and end point)
#-start at 2000
#-loop through each number and test to see if it is cleanly divisble by 7 (use modulo operator)
#-if the number is divisible by 7 test to make sure it is not a muliple of 5 (again use the modulo operator...I think) 

##Solution:
#def numFind(start,end):
#	numList = []
#	for x in range(start,end):
#		if x % 7 == 0 and x % 5 != 0:
#			numList.append(x)
#	
#	for i in numList:
#		print(i,end=",")
#
#numFind(2000,3200)

#Question 2:
#Write a program which can compute the factorial of a given number.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

#Notes:
#-equation for finding factorial of a number is n!= n*(n-1)!
#-I can easily build a loop to find a numbers factorial
#-8! = 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8
#-y = 1 will be my starting place
#-while x will be my multiplier

def factorial(x):
	y = 1
	while x > 1:
		y = y * x
		x = x - 1

	print(y)

factorial(3)






