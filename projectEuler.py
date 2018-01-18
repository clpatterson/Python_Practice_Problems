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


##My Solution:
#def evenFibsum():
#	fibs = [0,1] #list of fibonacci numbers
#	max_fib = 4000000 #fibonacci numbers in our sequence must be under four million
#
#	while fibs[-2] + fibs[-1] < max_fib:
#		newFib = fibs[-2] + fibs[-1]
#		fibs.append(newFib)
#		evenFibs = [x for x in fibs if x % 2 == 0]
#
#	result = sum(evenFibs)
#	print(result)
#
#evenFibsum()

#Problem 3: Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143

#Notes:
#1) I need to create a program that takes any number as input and outputs its prime factors
#Prime numbers:
#-How the fuck do I do that? What is the process of finding prime factors?
#-A prime number is a number that can only be divided by itself and one. 
#-A prime number must be a whole number greater than 1.
#Prime Factorization:
#-Prime factorization is the process of finding which prime numbers multiply together
#to make the original number. 
#-With an input number it is best to start dividing by
#the smallest prime number and working your way up through the list. The smallest
#prime number is 2 and then 3, etc.
#To factorize we take the number n and start by dividing it by the smallest prime number.
#If n is divisable by 2, we store 2 as a prime factor of the number,
#then we test the quotient for primeness. If the quotient is prime, 
#we store it as a prime factor of n in a list, and our prime factorization is done.  
#If the quotient is not prime, we begin the process of dividing by the smallest prime number again.
#Where is the loop?
#Prime factorization continues until the quotient is a prime factor, so I can use a while loop here 
#Prime number list:
#-to do prime factorization I'll need a list of prime numbers...
#-but if my program will be able to determine the prime factorization for any number,
#the list of prime numbers will have to be larger or smaller to accomodate the size of the 
#input number.
#-Do I need to first run a test on the input number to determine how large it is and thus 
#how many prime factors I'll need? Or can I just derive a method to create prime numbers as I
#need them in the prime factorization process? That seems reasonable...
#What are my steps?
#1) write a test to see if a number is prime, then store that number in variable or list, etc
#2) now take any number as an input and conduct prime factorization


##My Solution:
#def primeTest(x): #takes input of number and tests to see if it is prime.
#	if type(x) == float: #add exception for floats 
#		x = 'error: may not be type <int>'
#		print(x)
#		return x
#
#	if x <= 1: #add exception if x is easily identified as not prime
#		x = 'not prime'
#		return x
#
#	for i in range(1,x+1): #loops through all potential factors to determine primeness
#		if x % i == 0:
#			if not(i == x) and not(i == 1):
#				x = 'not prime'
#				return x
#	x = 'prime'
#	return x
#
#
#def primeFinder(start,end): 
#	primes = [] #initialize my output list of all prime numbers
#	if end <= 1: #ensures that range will include at least one prime number 
#		print('Input a max number greater than 1.')
#		return
#
#	for x in range(start,end+1): #loops through to creates prime list
#		if primeTest(x) == 'prime':
#			primes.append(x)
#
#	return primes
#
#
#
#def primeFactorize(n):
#	factors = [] #initialize my output list of final factors for given number
#	x = 0
#	y = 100
#	primeList = primeFinder(x,y) #generates starting list of potential prime factors
#	current_prime = 0 #place holder used for navigating list of potential prime factors
#	
#	while primeTest(n) == 'not prime':
#		try: #test to see end of potential prime factors list has been reached 
#			check = primeList[current_prime]
#		except IndexError: #generate more potential prime factors and add to list
#			x = x + 100
#			y = y + 100
#			primeList_extend = primeFinder(x,y)
#			primeList = primeList + primeList_extend
#				
#		if n % primeList[current_prime] == 0: #check to make sure n is divisble by this prime
#			n = n//primeList[current_prime] #save n as quotient of n/current_prime
#			factors.append(primeList[current_prime]) #add prime to factors list
#			if primeTest(n) == 'prime':
#				factors.append(n) #save final prime factor before loop terminates
#		else:
#			current_prime = current_prime + 1 #prepare to try the next potential prime factor
#
#	return(factors)
#
#
#def largestPrime_factor(someNumber):
#	result = primeFactorize(someNumber)[-1] #grab the last and largest prime factor in the ordered list
#	print(result) #print value, hurray!!!
#	return result
#
#largestPrime_factor(600851475143)

	




		











