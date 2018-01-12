#Question:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
#notes:
#-input of this program is a range (a start and end point)
#-start at 2000
#-loop through each number and test to see if it is cleanly divisble by 7 (use modulo operator)
#-if the number is divisible by 7 test to make sure it is not a muliple of 5 (again use the modulo operator...I think) 
def numFind(start,end):
	numList = []
	for x in range(start,end):
		if x % 7 == 0 and x % 5 != 0:
			numList.append(x)
	
	for i in numList:
		print(i,end=",")

numFind(2000,3200)


