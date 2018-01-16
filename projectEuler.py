#Below are my solutions to Project Euler problems
#Spoiler Alert! 

#Problem 2: Even Fibonacci numbers
#By considering the terms in the Fibbonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.

#Notes:
#1) create a program that finds Fibonacci numbers
#2) create a loop to test whether value of the last term is under four million
#3) use a list to store all the even terms (test for evenness) 
#4) cycle through the list and sum all the numbers 
#5) print the final answer
#I might be able to do this using list functions. So I start with a list with 0 and 1,
#then just add mylist[:-1] and mylist[:-2]

#My Solution:
def evenFibsum():
	fibs = [0,1] #list of fibonacci numbers
	max_fib = 4000000 #fibonacci numbers in our sequence must be under four million

	while fibs[-2] + fibs[-1] < max_fib:
		newFib = fibs[-2] + fibs[-1]
		fibs.append(newFib)
		evenFibs = [x for x in fibs if x % 2 == 0]

	result = sum(evenFibs)
	print(result)

evenFibsum()







